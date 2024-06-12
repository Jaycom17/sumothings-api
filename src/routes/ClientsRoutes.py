from flask import Blueprint
from controllers.ClientsCotroller import getClients, getClient, postClient, putClient, dropClient, loginClient

def setupRoutesClients(app):
    bp = Blueprint('client', __name__)
    
    # Rutas para CRUD de clientes
    bp.route('/client', methods=['GET'])(getClients)
    bp.route('/client/<string:cliId>', methods=['GET'])(getClient)
    bp.route('/client', methods=['POST'])(postClient)
    bp.route('/client/<string:cliId>', methods=['PUT'])(putClient)
    bp.route('/client/<string:cliId>', methods=['DELETE'])(dropClient)
    bp.route('/loginClient', methods=['POST'])(loginClient)
    
    app.register_blueprint(bp)