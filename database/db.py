import pymongo
from flask import current_app, g

class Database:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client.get_database()
        
    def get_collection(self, collection_name):
        return self.db[collection_name]
    
def get_db():
        if 'db' not in g:
            g.db = Database(
                uri=current_app.config["MONGO_URI"],
               
            )

        return g.db
    
def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.client.close()


# users_collection = db.get_collection('users').

# Just to verify connection