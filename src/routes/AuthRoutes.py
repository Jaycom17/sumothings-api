from flask import Blueprint
from controllers.AuthController import login, logout, loginAdmin, validateAdmin, validateClient

def setupRoutesAuth(app):
    bp = Blueprint('auth', __name__)
    
    # Rutas para CRUD de items
    bp.route('/login', methods=['POST'])(login)
    bp.route('/login-admin', methods=['POST'])(loginAdmin)
    bp.route('/logout', methods=['GET'])(logout)
    bp.route('/validate-admin', methods=['POST'])(validateAdmin)
    bp.route('/validate-client', methods=['POST'])(validateClient)
    
    app.register_blueprint(bp)