from flask import Flask
from routes.AuthRoute import main as AuthRoute
from routes.TaskRoute import main as TaskRoute
from database.db import close_db



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    #cierra la conexion a la db al finalizar la app
    app.teardown_appcontext(close_db)
    
    #importar rutas
    app.register_blueprint(AuthRoute,url_prefix='/api/auth')
    app.register_blueprint(TaskRoute,url_prefix='/api/tasks')
    return app