# IMPORTS
from flask import Flask, jsonify, request

# SERVICIOS
from services.user import user

# CONTROLADOR


class user_controller:
    # CONSTRUCTOR
    def __init__(self, app):
        self.user_service = user()
        self.set_routes(app)

    # RUTAS
    def set_routes(self, app):
        @app.route('/user', methods=['POST'])
        @app.validate( 'user', 'data' )
        def set_user():
            return self.user_service.set_data(request.json)