from flask import Blueprint
from controllers.ArticlesController import getArticles, getArticle, postArticle, putArticle, dropArticle

def setupRoutesArticle(app):
    bp = Blueprint('articles', __name__)

    # Rutas para CRUD de articulos
    bp.route('/articles', methods=['GET'])(getArticles)
    bp.route('/articles/<string:articleID>', methods=['GET'])(getArticle)
    bp.route('/articles', methods=['POST'])(postArticle)
    bp.route('/articles/<string:articleID>', methods=['PUT'])(putArticle)
    bp.route('/articles/<string:articleID>', methods=['DELETE'])(dropArticle)
    
    app.register_blueprint(bp)