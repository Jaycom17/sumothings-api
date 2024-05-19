from flask import Blueprint
from controllers.DealersController import postDealer, dropDealer, getDealer, getDealers, putDealer

def setupRoutesDealer(app):
    bp = Blueprint('dealers', __name__)
    
    # Rutas para CRUD de items
    bp.route('/dealer', methods=['GET'])(getDealers)
    bp.route('/dealer/<string:dealerId>', methods=['GET'])(getDealer)
    bp.route('/dealer', methods=['POST'])(postDealer)
    bp.route('/dealer/<string:dealerId>', methods=['PUT'])(putDealer)
    bp.route('/dealer/<string:dealerId>', methods=['DELETE'])(dropDealer)
    
    app.register_blueprint(bp)