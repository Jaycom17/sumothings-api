from flask import request, jsonify
from middlewares.ShoppingMiddleware import postShoppingMiddleWare, putShoppingMiddleWare
from services.ShoppingServices import getAllShoppings, getShoppingById, createShopping, updateShopping, deleteShopping
from middlewares.AuthMiddleware import verifyAdmin

def getShoppings():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    shoppings = getAllShoppings()
    
    if shoppings == None:
        return jsonify({"error": "An error occurred while getting all shoppings"}), 500
    
    return shoppings, 200

def getShopping(shoId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    shopping = getShoppingById(shoId)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while getting all shoppings"}), 500
    
    return shopping, 200

def postShopping():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        shoppingsToCreate = postShoppingMiddleWare(request.get_json())

        if shoppingsToCreate == None:
            return jsonify({"error": "Invalid body"}), 400
        
        for shoppingToCreate in shoppingsToCreate:
            shopping = createShopping(shoppingToCreate)
        
        return jsonify(shopping), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while creating a shopping"}), 500

def putShopping(shoId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        shoppingsToUpdate = putShoppingMiddleWare(request.get_json(), shoId)

        if shoppingsToUpdate == None:
            return jsonify({"error": "Invalid body"}), 400
        
        for shoppingToUpdate in shoppingsToUpdate:
            shopping = updateShopping(shoppingToUpdate.shoID, shoppingToUpdate)    
        
        return jsonify(shopping), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating a shopping"}), 500

def dropShopping(shoId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401

    shopping = deleteShopping(shoId)
    
    if shopping == None:
        return jsonify({"error": "An error occurred while deleting a shopping"}), 500
    
    return jsonify(shopping), 200