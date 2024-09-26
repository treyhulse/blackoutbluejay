import os
from pymongo import MongoClient
import os
from pymongo import MongoClient

# Function to get the MongoDB client
def get_mongo_connection():
    # Fetch the connection string and database name from Heroku environment variables
    mongo_connection_string = os.environ.get("mongo_connection_string")
    db_name = os.environ.get("db")
    
    # Create a MongoDB client
    client = MongoClient(mongo_connection_string)
    
    # Connect to the specified database
    db = client[db_name]
    
    return db


# Example of how to use the connection
def get_collection(collection_name):
    db = get_mongo_connection()
    return db[collection_name]
