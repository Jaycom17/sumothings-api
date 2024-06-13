from flask import request, jsonify
from services.ArticlesServices import getAllArticles ,getArticleById, createArticle, updateArticle, deleteArticle
from middlewares.ArticleMiddleware import articleMiddleWare
from middlewares.AuthMiddleware import verifyAdmin

def getArticles():

    articles = getAllArticles()
    
    if articles == None:
        return jsonify({"error": "An error occurred while getting all articles"}), 500
    
    return articles, 200
def getArticle(articleID):
    
    article = getArticleById(articleID)
    
    if article == None:
        return jsonify({"error": "An error occurred while getting the article"}), 500
    
    return article, 200
def postArticle():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401

    articleToCreate = articleMiddleWare(request.get_json())

    if articleToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    article = createArticle(articleToCreate)
    
    if article == None:
        return jsonify({"error": "An error occurred while creating a article"}), 500
    
    return jsonify(article), 200
def putArticle(articleID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    articleToUpdate = articleMiddleWare(request.get_json())
    
    if articleToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    article = updateArticle(articleID, articleToUpdate)
    
    if article == None:
        return jsonify({"error": "An error occurred while updating a article"}), 500
    
    return jsonify(article), 200
def dropArticle(articleID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
        
    article = deleteArticle(articleID)
    
    if article == None:
        return jsonify({"error": "An error occurred while deleting a article"}), 500
    
    return jsonify(article), 200