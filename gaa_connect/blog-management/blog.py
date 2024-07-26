from typing import Optional, List
from uuid import uuid4
from datetime import datetime


class BlogPost:

    def __init__(self, title: str, content: str, author: str):

        self.post_id = str(uuid4())
        self.author = author
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.comments = []

    def to_dict(self):
        return {
            "post_id": self.post_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),  # Convert datetime to ISO 8601 string
            "comments": self.comments  # List of comments, already in dictionary format
        }
