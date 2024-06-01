from flask import Blueprint
from controllers.TypesController import getTypes, getType, postType, putType, dropType

def setupRoutesType(app):
    bp = Blueprint('types', __name__)

    # Rutas para CRUD de tipos
    bp.route('/types', methods=['GET'])(getTypes)
    bp.route('/types/<string:typeID>', methods=['GET'])(getType)
    bp.route('/types', methods=['POST'])(postType)
    bp.route('/types/<string:typeID>', methods=['PUT'])(putType)
    bp.route('/types/<string:typeID>', methods=['DELETE'])(dropType)
    
    app.register_blueprint(bp)