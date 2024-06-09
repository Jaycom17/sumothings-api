from flask import Blueprint
from controllers.AuthController import login

def setupRoutesDealer(app):
    bp = Blueprint('dealers', __name__)
    
    # Rutas para CRUD de items
    bp.route('/login', methods=['POST'])(login)
    
    app.register_blueprint(bp)