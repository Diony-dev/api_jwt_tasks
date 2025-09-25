from flask import Blueprint, request, jsonify
from services.taskservices import create_task, get_tasks_by_user, get_task_bay_id, update_task, delete_task
from utils.security import token_required


main = Blueprint('task', __name__)

@main.route('/tasks', methods=['POST'])
@token_required
def create_new_task(user_id):
    data = request.get_json()
    data['id_usuario'] = user_id
    task = create_task(data)
    return jsonify({"message": "Tarea creada con éxito", "task": task.to_dict()}), 201


@main.route('/tasks', methods=['GET'])
@token_required
def get_tasks(user_id):
    tasks = get_tasks_by_user(user_id)
    if not tasks:
        return jsonify({"message": "No se encontraron tareas"}), 404
    return jsonify({"message": "Tareas obtenidas con éxito", "tasks":tasks}), 200


@main.route('/tasks/<task_id>', methods=['GET'])
@token_required
def get_task(user_id, task_id):
    task = get_task_bay_id(task_id)
    if not task or str(task.id_usuario) != user_id:
        return jsonify({"message": "Tarea no encontrada"}), 404
    return jsonify({"message": "Tarea obtenida con éxito", "task": task.to_dict()}), 200


@main.route('/tasks/<task_id>', methods=['PUT'])
@token_required
def update_existing_task(user_id, task_id):
    task = get_task_bay_id(task_id)
    if not task or str(task.id_usuario) != user_id:
        return jsonify({"message": "Tarea no encontrada"}), 404
    data = request.get_json()
    success = update_task(task_id, data)
    if not success:
        return jsonify({"message": "No se pudo actualizar la tarea"}), 500
    return jsonify({"message": "Tarea actualizada con éxito"}), 200


@main.route('/tasks/<task_id>', methods=['DELETE'])
@token_required
def delete_existing_task(user_id, task_id):
    task = get_task_bay_id(task_id)
    if not task or str(task.id_usuario) != user_id:
        return jsonify({"message": "Tarea no encontrada"}), 404
    success = delete_task(task_id)
    if not success:
        return jsonify({"message": "No se pudo eliminar la tarea"}), 500
    return jsonify({"message": "Tarea eliminada con éxito"}), 200