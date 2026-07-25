import os
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
if "mongodb+srv" in MONGO_URI or "mongodb.net" in MONGO_URI:
    client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
else:
    client = MongoClient(MONGO_URI)

# Database
db = client["mood_db"]

# Collections
users_collection = db["users"]
mood_history_collection = db["mood_history"]