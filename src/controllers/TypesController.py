from flask import request, jsonify
from middlewares.TypesMiddleware import typesMiddleware
from services.TypesServices import createProductType, deleteProductType, getAllProductTypes, getProductTypeById, updateProductType

def getTypes():
    types = getAllProductTypes()
    
    if types == None:
        return jsonify({"error": "An error occurred while getting all types"}), 500
    
    return types, 200

def getType(typeID):
    type = getProductTypeById(typeID)
    
    if type == None:
        return jsonify({"error": "An error occurred while getting the type"}), 500
    
    return type, 200

def postType():
    typeToCreate = typesMiddleware(request.get_json())

    if typeToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    type = createProductType(typeToCreate)
    
    if type == None:
        return jsonify({"error": "An error occurred while creating a type"}), 500
    
    return jsonify(type), 200

def putType(typeID):
    typeToUpdate = typesMiddleware(request.get_json())
    
    if typeToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    type = updateProductType(typeID, typeToUpdate)
    
    if type == None:
        return jsonify({"error": "An error occurred while updating a type"}), 500
    
    return jsonify(type), 200

def dropType(typeID):
    type = deleteProductType(typeID)
    
    if type == None:
        return jsonify({"error": "An error occurred while deleting a type"}), 500
    
    return jsonify(type), 200