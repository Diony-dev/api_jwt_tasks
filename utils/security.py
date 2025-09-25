from functools import wraps
from flask import request, jsonify
from .jwt_manager import verify_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"message":"Token no proporcionado"}),401
        token = auth_header.split(" ")[1]
        user_id = verify_token(token)
        if not user_id:
            return jsonify({"message":"Token inválido o expirado"}),401
        return f(user_id, *args, **kwargs)
    return decorated
        
            