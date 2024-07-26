from dotenv import load_dotenv
import os
from pymongo.collection import Collection

from User import User

from pymongo import MongoClient


def write_new_user(user: User, user_collection: Collection):
    insert_result = user_collection.insert_one(user.to_dict())

    if insert_result:
        print("Successfully inserted")
    else:
        print("Failure to insert :(")


def delete_user():
    ...


def follow_new_user(base_user_id: str, follow_user_id: str, user_collection: Collection):
    base_user = user_collection.find_one({"user_id": base_user_id})
    followed_user = user_collection.find_one({"user_id": follow_user_id})

    if not base_user:
        print(f"No user found with base user id - {base_user_id}")
        return

    if not followed_user:
        print(f"Cannot follow user {follow_user_id} as there is no account with that user_id")
        return

    follow_list = list(base_user["following"])

    if follow_user_id not in follow_list:
        follow_list.append(follow_user_id)
        user_collection.update_one({"user_id": base_user_id}, {"$set": {"following": follow_list}})
        print(f"Account {base_user_id} followed {follow_user_id}")
    else:
        print(f"Could not follow user {follow_user_id} - account is already followed")


def unfollow_user(base_user_id: str, unfollow_user_id: str, user_collection: Collection):
    base_user = user_collection.find_one({"user_id": base_user_id})
    followed_user = user_collection.find_one({"user_id": unfollow_user_id})

    if not base_user:
        print(f"No user found with base user id - {base_user_id}")
        return

    if not followed_user:
        print(f"Cannot unfollow user {unfollow_user_id} as there is no account with that user_id")
        return

    follow_list = list(base_user["following"])
    if unfollow_user_id not in follow_list:
        print(f"Cannot unfollow user {unfollow_user_id} as this account is not followed")
    else:
        follow_list.remove(unfollow_user_id)
        user_collection.update_one({"user_id": base_user_id}, {"$set": {"following": follow_list}})
        print(f"User {base_user_id} unfollowed {unfollow_user_id}")


if __name__ == "__main__":

    cian = User(
        username="oisin",
        email="oisin@gmail.com",
        password="oisin",
        bio="Hello World",
        club="Dungloe",
        county="Donegal"
    )

    load_dotenv()

    uri = os.getenv("MONGODB_CONNECTION_URI")
    database_name = os.getenv("MONGODB_DATABASE_NAME")
    user_collection = os.getenv("USER_COLLECTION_NAME")

    # Create a new client and connect to the server
    client = MongoClient(uri)
    database = client[database_name]
    users_collection = database[user_collection]

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # write_new_user(
    #     user=cian,
    #     user_collection=users_collection
    # )

    # follow_new_user(
    #     base_user_id="filler",
    #     follow_user_id="filler",
    #     user_collection=users_collection
    # )

    # unfollow_user(
    #     base_user_id="filler",
    #     unfollow_user_id="filler",
    #     user_collection=users_collection
    # )
