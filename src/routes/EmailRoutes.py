from flask import Blueprint
from controllers.EmailController import sendEmail

def setupRoutesEmail(app):
    bp = Blueprint('email', __name__)
    
    # Rutas para CRUD de items
    bp.route('/send-email', methods=['POST'])(sendEmail)
    
    app.register_blueprint(bp)