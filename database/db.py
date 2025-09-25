import pymongo
from flask import current_app, g
import os

class Database:
    def __init__(self, uri, db_name=None):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client.get_database(db_name)

    def get_collection(self, collection_name):
        return self.db[collection_name]
    
def get_db():
        if 'db' not in g:
            g.db = Database(
                uri=current_app.config["MONGO_URI"],
                db_name=os.environ.get('MONGODB_DB_NAME')
            )

        return g.db
    
def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.client.close()


# users_collection = db.get_collection('users').

# Just to verify connection