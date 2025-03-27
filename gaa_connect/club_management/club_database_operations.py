from gaa_connect.club_management.club import Club
from pymongo.collection import Collection

def insert_new_club(new_club: Club, club_collection: Collection) -> bool:
    try:
        result = club_collection.insert_one(new_club.to_dict())
        return result.inserted_id is not None
    except Exception as e:
        print(f"Error inserting club: {e}")
        return False

