from flask import Blueprint

def setupRoutesDealer(app):
    bp = Blueprint('dealers', __name__)
    
    # Rutas para CRUD de items
    bp.route('/login', methods=['POST'])(getDealers)
    bp.route('/validateadmin', methods=['GET'])(getDealer)
    bp.route('/profile', methods=['GET'])(postDealer)
    bp.route('/dealer/<string:dealerId>', methods=['PUT'])(putDealer)
    bp.route('/dealer/<string:dealerId>', methods=['DELETE'])(dropDealer)
    
    app.register_blueprint(bp)