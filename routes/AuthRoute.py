from flask import Blueprint, request, jsonify
from services.auth import insert_user, get_user, get_user_by_id,verify_password
from utils.jwt_manager import generate_token
from utils.security import token_required

main = Blueprint('main',__name__)


@main.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    registerUser = get_user(data)
    if registerUser:
        return jsonify({"message":"User already exists"}), 409
    user_id = insert_user(data)
    main.logger.info(f'Nuevo usuario registrado con ID: {user_id}')
    return jsonify({"message":"User registered successfully", "user_id": user_id}), 201

@main.route('/info',methods=['GET'])
@token_required
def info(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"message":"User not found"}), 404
    main.logger.info(f'Información del usuario recuperada con ID: {user_id}')
    return jsonify(user.to_dict()), 200

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = get_user(data)
    if not user or not verify_password(user.password, data.get('password')):
        return jsonify({"message":"Invalid username or password"}), 401
    token = generate_token(str(user.id))
    return jsonify({"message":"Login successful", "token": token}), 200