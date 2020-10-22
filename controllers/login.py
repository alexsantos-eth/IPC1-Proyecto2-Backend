# IMPORTS
from flask import request

# SERVICIOS
from services.login import login

# CONTROLADOR


class login_controller:
    # CONSTRUCTOR
    def __init__(self, app):
        self.login_service = login()
        self.set_routes(app)

    # RUTAS
    def set_routes(self, app):
        @app.route('/login', methods=['POST'])
        @app.validate('user', 'login')
        def login_user():
            # AGREGAR USUARIOS
            loginData = request.json
            return self.login_service.login_user(loginData['user_name'], loginData['password'])