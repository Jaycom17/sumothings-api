from flask import Blueprint
from controllers.ShoppingsController import getShoppings, getShopping, postShopping, putShopping, dropShopping

def setupRoutesShopping(app):
    bp = Blueprint('shopping', __name__)
    
    # Rutas para CRUD de items
    bp.route('/shopping', methods=['GET'])(getShoppings)
    bp.route('/shopping/<string:shoId>', methods=['GET'])(getShopping)
    bp.route('/shopping', methods=['POST'])(postShopping)
    bp.route('/shopping/<string:shoId>', methods=['PUT'])(putShopping)
    bp.route('/shopping/<string:shoId>', methods=['DELETE'])(dropShopping)
    
    app.register_blueprint(bp)