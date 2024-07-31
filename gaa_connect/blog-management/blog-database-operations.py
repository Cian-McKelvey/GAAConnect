from datetime import datetime
from uuid import uuid4

from pymongo.collection import Collection
from pymongo.errors import PyMongoError

from blog import BlogPost


def write_new_blogpost(blogpost: BlogPost, blog_collection: Collection):
    # Todo: Make this an admin feature
    insert_result = blog_collection.insert_one(blogpost.to_dict())
    if insert_result:
        print(f"{blogpost.title} has been added to the database")
    else:
        print(f"{blogpost.title} could not be added to the database")


def edit_existing_blogpost_title(blog_collection: Collection, blogpost_id: str, new_title: str):
    # Todo: Make this an admin feature
    update_result = blog_collection.update_one(
        {"blogpost_id": blogpost_id},
        {"$set": {"title": new_title}}
    )

    if update_result.matched_count == 0:
        print("No blogpost found with that id")
        return

    if update_result.modified_count > 0:
        print("Title has been updated")
    else:
        print("Title could not be updated")


def edit_existing_blogpost_content(blog_collection: Collection, blogpost_id: str, new_content: str):
    # Todo: Make this an admin feature
    update_result = blog_collection.update_one(
        {"blogpost_id": blogpost_id},
        {"$set": {"content": new_content}}
    )

    if update_result.matched_count == 0:
        print("No blogpost found with that id")
        return

    if update_result.modified_count > 0:
        print("Content has been updated")
    else:
        print("Content could not be updated")


def delete_existing_blogpost(blog_collection: Collection, blogpost_id: str):
    # Todo: Make this an admin feature
    delete_result = blog_collection.delete_one({"blogpost_id": blogpost_id})

    if delete_result.deleted_count > 0:
        print("Blogpost was deleted successfully")
    else:
        print("Blogpost could not be deleted")


def add_comment_to_blogpost(blogpost_id: str, commenter_id: str, comment_text: str,
                            blog_collection: Collection, user_collection: Collection):
    # Find blogpost and verify its there
    blogpost = blog_collection.find_one({"blogpost_id": blogpost_id})
    if not blogpost:
        print("No blogpost with id: " + blogpost_id)
        return

    # Add a check to make sure the user with the commenter id is valid
    commenter = user_collection.find_one({"user_id": commenter_id})
    if not commenter:
        print("Comment ID is not valid, comment could not be added to blogpost")
        return

    # Fetch the comments list
    comments_list = list(blogpost["comments"])
    # Append the new comment to the comments list
    new_comment = {
        "comment_id": str(uuid4()),
        "username": commenter["username"],
        "comment_text": comment_text,
        "commenter_id": commenter_id,
        "created_at": datetime.now().isoformat()
    }
    comments_list.append(new_comment)

    # Update the item in the database to use the new comment
    try:
        update_result = blog_collection.update_one({"blogpost_id": blogpost_id}, {"$set": {"comments": comments_list}})
        if update_result.modified_count > 0:
            print("Comment has been added to blogpost")
        else:
            print("Comment could not be added to blogpost")

    except PyMongoError as err:
        print("Error Occurred while writing new comment: " + str(err))


def update_blogpost_comment(blog_collection: Collection, blogpost_id: str, comment_id: str, updated_content: str):
    # Find the blog post and the specific comment within it
    filter_query = {
        "blogpost_id": blogpost_id,
        "comments.comment_id": comment_id
    }

    # Define the update operation
    update_operation = {
        "$set": {
            "comments.$.comment_text": updated_content
        }
    }

    # Perform the update
    update_result = blog_collection.update_one(filter_query, update_operation)

    # Check the result and provide feedback
    if update_result.matched_count == 0:
        print("No blogpost or comment found with the specified ids")
    elif update_result.modified_count > 0:
        print("Comment was updated successfully")
    else:
        print("Comment text was not modified")


def delete_comment_from_blogpost(blog_collection: Collection, blogpost_id: str, comment_id: str):
    # Find blogpost and verify its there
    blogpost = blog_collection.find_one({"blogpost_id": blogpost_id})
    if not blogpost:
        print("No blogpost with id: " + blogpost_id)
        return

    # Fetch the comments list
    comments_list = list(blogpost["comments"])
    comment_found = False
    for index, content in enumerate(comments_list):
        if content["comment_id"] == comment_id:
            comment_found = True
            comments_list.pop(index)

    if not comment_found:
        print("Comment not found: " + comment_id)
        return

    try:
        update_result = blog_collection.update_one({"blogpost_id": blogpost_id}, {"$set": {"comments": comments_list}})
        if update_result.modified_count > 0:
            print("Comment has been deleted from blogpost")
        else:
            print("Comment could not be deleted from blogpost")

    except PyMongoError as err:
        print("Error Occurred while deleting comment: " + str(err))
