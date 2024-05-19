from flask import request, jsonify
from middlewares.ShoppingMiddleware import shoppingMiddleWare
from services.ShoppingServices import getAllShoppings, getShoppingById, createShopping, updateShopping, deleteShopping

def getShoppings():
    
    shoppings = getAllShoppings()
    
    if shoppings == None:
        return jsonify({"error": "An error occurred while getting all shoppings"}), 500
    
    return shoppings, 200

def getShopping(shoId):
    
    shopping = getShoppingById(shoId)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while getting all shoppings"}), 500
    
    return shopping, 200

def postShopping():
    shoppingToCreate = shoppingMiddleWare(request.get_json())

    if shoppingToCreate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    shopping = createShopping(shoppingToCreate)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while creating a shopping"}), 500
    
    return jsonify(shopping), 200

def putShopping(shoId):
    shoppingToUpdate = shoppingMiddleWare(request.get_json())

    if shoppingToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    shopping = updateShopping(shoId, shoppingToUpdate)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while updating a shopping"}), 500
    
    return jsonify(shopping), 200

def dropShopping(shoId):

    shopping = deleteShopping(shoId)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while deleting a shopping"}), 500
    
    return jsonify(shopping), 200