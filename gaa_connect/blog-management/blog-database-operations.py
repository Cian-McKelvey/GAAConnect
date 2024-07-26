def add_comment_to_blogpost(blogpost_id: str, commenter_id: str, comment_text: str):
    # Find blogpost and verify its there

    # Fetch the comments list

    # Append the new comment to the comments list

    # Update the item in the database to use the new comment

    """ Comment format is below - this isn't guaranteed to be correct
        comments.append({
            "comment_id": str(uuid4()),
            "comment": comment,
            "commenter": commenter,
            "created_at": datetime.now().isoformat()
        })
    """
    ...