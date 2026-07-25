from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["mood_db"]

# Collections
users_collection = db["users"]
mood_history_collection = db["mood_history"]