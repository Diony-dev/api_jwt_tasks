from database.db import get_db
from models.tarea import Tarea
from bson.objectid import ObjectId

def create_task(taskdata):
    db = get_db()
    task_collection = db.get_collection('tareas')
    result = task_collection.insert_one({
        'titulo':taskdata['titulo'],
        'descripcion':taskdata['descripcion'],
        'estado':taskdata['estado'],
        'id_usuario':ObjectId(taskdata['id_usuario'])
    })
    task = Tarea(
        _id=result.inserted_id,
        titulo=taskdata['titulo'],
        descripcion=taskdata['descripcion'],
        estado=taskdata['estado'],
        id_usuario=ObjectId(taskdata['id_usuario'])
    )
    return task


def get_tasks_by_user(user_id):
    db = get_db()
    task_collection = db.get_collection('tareas')
    tasks = task_collection.find({"id_usuario": ObjectId(user_id)})
    return [Tarea(**task).to_dict() for task in tasks]


def get_task_bay_id(task_id):
    db = get_db()
    task_collection = db.get_collection('tareas')
    task_data = task_collection.find_one({"_id": ObjectId(task_id)})
    if task_data:
        return Tarea(**task_data)
    return None

def update_task(task_id, taskdata):
    db = get_db()
    task_collection = db.get_collection('tareas')
    result = task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": taskdata}
    )
    return result.modified_count > 0

def delete_task(task_id):
    db = get_db()
    task_collection = db.get_collection('tareas')
    result = task_collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count > 0

