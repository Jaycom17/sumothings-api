from flask import Blueprint
from controllers.AdminUsersController import getAdminUsers, getAdminUser, postAdminUser, putAdminUser, dropAdminUser

def setupRoutesAdminUser(app):
    bp = Blueprint('adminUser', __name__)
    
    # Rutas para CRUD de usuarios administradores
    bp.route('/adminUser', methods=['GET'])(getAdminUsers)
    bp.route('/adminUser/<string:admID>', methods=['GET'])(getAdminUser)
    bp.route('/adminUser', methods=['POST'])(postAdminUser)
    bp.route('/adminUser', methods=['PUT'])(putAdminUser)
    bp.route('/adminUser/<string:admID>', methods=['DELETE'])(dropAdminUser)
    
    app.register_blueprint(bp)
