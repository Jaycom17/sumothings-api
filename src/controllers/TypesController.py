from flask import request, jsonify
from middlewares.TypesMiddleware import typesMiddleware
from services.TypesServices import createProductType, deleteProductType, getAllProductTypes, getProductTypeById, updateProductType
from middlewares.AuthMiddleware import verifyAdmin

def getTypes():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    types = getAllProductTypes()
    
    if types == None:
        return jsonify({"error": "An error occurred while getting all types"}), 500
    
    return types, 200

def getType(typeID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    type = getProductTypeById(typeID)
    
    if type == None:
        return jsonify({"error": "An error occurred while getting the type"}), 500
    
    return type, 200

def postType():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    typeToCreate = typesMiddleware(request.get_json())

    if typeToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    type = createProductType(typeToCreate)
    
    if type == None:
        return jsonify({"error": "An error occurred while creating a type"}), 500
    
    return jsonify(type), 200

def putType(typeID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    typeToUpdate = typesMiddleware(request.get_json())
    
    if typeToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    type = updateProductType(typeID, typeToUpdate)
    
    if type == None:
        return jsonify({"error": "An error occurred while updating a type"}), 500
    
    return jsonify(type), 200

def dropType(typeID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    type = deleteProductType(typeID)
    
    if type == None:
        return jsonify({"error": "An error occurred while deleting a type"}), 500
    
    return jsonify(type), 200