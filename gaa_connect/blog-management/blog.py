from uuid import uuid4
from datetime import datetime


class BlogPost:

    def __init__(self, title: str, content: str, author: str):

        self.blogpost_id = str(uuid4())
        self.author = author
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.comments = []

    def to_dict(self):
        return {
            "blogpost_id": self.blogpost_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),  # Convert datetime to ISO 8601 string
            "comments": self.comments  # List of comments, already in dictionary format
        }

    def __str__(self):
        return (
            f"title={self.title}, author={self.author}, "
            f"created_at={self.created_at.isoformat()}, comments_count={len(self.comments)})"
        )
