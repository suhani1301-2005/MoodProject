"""
Script to migrate database from Local MongoDB to MongoDB Atlas Cloud.

Usage:
1. Set target cloud URI:
   $env:MONGO_URI="mongodb+srv://<user>:<password>@cluster.mongodb.net/..."
2. Run script:
   python export_import_mongo.py
"""

import os
from pymongo import MongoClient

LOCAL_URI = "mongodb://localhost:27017/"
CLOUD_URI = os.getenv("TARGET_MONGO_URI", "mongodb+srv://suhanisaxena014_db_user:nkHA8hwnE9NixF4M@cluster0.0ft7xpo.mongodb.net/?appName=Cluster0")

def migrate():
    if not CLOUD_URI:
        print("ERROR: Please set TARGET_MONGO_URI environment variable before running.")
        print("Example: $env:TARGET_MONGO_URI='mongodb+srv://username:password@cluster.mongodb.net/'")
        return

    print("Connecting to Local MongoDB...")
    local_client = MongoClient(LOCAL_URI)
    local_db = local_client["mood_db"]

    print("Connecting to Cloud MongoDB Atlas...")
    cloud_client = MongoClient(CLOUD_URI, tlsAllowInvalidCertificates=True)
    cloud_db = cloud_client["mood_db"]

    for collection_name in ["users", "mood_history"]:
        docs = list(local_db[collection_name].find({}))
        if docs:
            print(f"Migrating {len(docs)} documents for collection '{collection_name}'...")
            cloud_db[collection_name].delete_many({}) # Clear old entries if re-running
            cloud_db[collection_name].insert_many(docs)
            print(f"Successfully migrated '{collection_name}'.")
        else:
            print(f"Collection '{collection_name}' is empty on local database.")

    print("\n✅ Database migration completed successfully!")

if __name__ == "__main__":
    migrate()
