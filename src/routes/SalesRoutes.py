from flask import Blueprint
from controllers.SalesController import getSales, getSale, postSale, putSale, deleteSale

def setupRoutesSales(app):
    bp = Blueprint('sales', __name__)
    
    # Rutas para CRUD de ventas
    bp.route('/sales', methods=['GET'])(getSales)
    bp.route('/sales/<string:salId>', methods=['GET'])(getSale)
    bp.route('/sales', methods=['POST'])(postSale)
    bp.route('/sales/<string:salId>', methods=['PUT'])(putSale)
    bp.route('/sales/<string:salId>', methods=['DELETE'])(deleteSale)
    
    app.register_blueprint(bp)
