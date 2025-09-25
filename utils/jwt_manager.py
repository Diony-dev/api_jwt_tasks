import jwt
from datetime import datetime, timedelta
from flask import current_app as app
import pytz


def generate_token(user_id):
    payload={
        'user_id':str(user_id),
        'exp':datetime.utcnow()+timedelta(hours=1),
        'iat':datetime.utcnow()
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None