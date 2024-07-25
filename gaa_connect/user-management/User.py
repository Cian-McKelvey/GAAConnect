from typing import Optional
from uuid import uuid4
import bcrypt
from datetime import datetime


class User:

    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 bio: Optional[str] = "",
                 club: Optional[str] = "",
                 county: Optional[str] = "",
                 is_private: bool = False):

        self.user_id = str(uuid4())
        self.username = username
        self.email = email
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.bio = bio
        self.club = club
        self.county = county
        self.is_private = is_private
        self.created_at = datetime.now()
        self.followers = []
        self.following = []
        self.posts = []

    def get_profile_info(self):
        return {
            "username": self.username,
            "bio": self.bio,
            "club": self.club,
            "county": self.county,
            "followers_count": len(self.followers),
            "following_count": len(self.following),
            "posts_count": len(self.posts),
        }

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "bio": self.bio,
            "club": self.club,
            "county": self.county,
            "is_private": self.is_private,
            "created_at": self.created_at.isoformat(),  # Convert datetime to ISO 8601 string
            "followers": self.followers,
            "following": self.following,
            "posts": self.posts,
        }
