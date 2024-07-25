from typing import Optional, List
from uuid import uuid4
from datetime import datetime


class BlogPost:

    def __init__(self, title: str, content: str):

        self.post_id = str(uuid4())
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.comments = []

    def add_comment(self, comment: str, commenter: str):
        self.comments.append({
            "comment_id": str(uuid4()),
            "comment": comment,
            "commenter": commenter,
            "created_at": datetime.now().isoformat()
        })
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "created_at": self.created_at.isoformat(),  # Convert datetime to ISO 8601 string
            "updated_at": self.updated_at.isoformat(),  # Convert datetime to ISO 8601 string
            "comments": self.comments  # List of comments, already in dictionary format
        }
