from dotenv import load_dotenv
import os
from pymongo.collection import Collection

from User import User

from pymongo import MongoClient


def write_new_user(user: User, user_collection: Collection):
    insert_result = user_collection.insert_one(user.to_dict())

    if insert_result:
        print("")
    else:
        print("")


def delete_user():
    ...


def follow_new_user(base_user_id: str, follow_user_id: str, user_collection: Collection):
    fetched_user = user_collection.find_one({"user_id": base_user_id})
    if fetched_user:
        follow_list = fetched_user["following"]
        print(type(follow_list))


if __name__ == "__main__":

    load_dotenv()

    uri = os.getenv("MONGODB_CONNECTION_URI")

    # Create a new client and connect to the server
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)