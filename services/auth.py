from database.db import get_db
from models.user import User
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


def insert_user(userdata):
    db = get_db()
    users_collection = db.get_collection('usuarios')
    result = users_collection.insert_one({
        'username': userdata['username'],
        'password': generate_password_hash(userdata['password']),
        'fullname': userdata.get('fullname'),
        'email': userdata.get('email')
        
    })
    return str(result.inserted_id)

def get_user(data):
    db = get_db()
    users_collection = db.get_collection('usuarios')
    user_data = users_collection.find_one({'username': data['username']})
    if user_data:
        return User(
            id=user_data.get('_id'),
            username=user_data.get('username'),
            password=user_data.get('password'),
            fullname=user_data.get('fullname'),
            email=user_data.get('email')
        )
    return None

def get_user_by_id(user_id):
    db = get_db()
    users_collection = db.get_collection('usuarios')
    user_data = users_collection.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(
            id=user_data.get('_id'),
            username=user_data.get('username'),
            password=user_data.get('password'),
            fullname=user_data.get('fullname'),
            email=user_data.get('email')
        )
    return None

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)