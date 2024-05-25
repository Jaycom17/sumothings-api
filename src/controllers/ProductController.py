from flask import request, jsonify, request
from services.ProductsServices import getProductById, getAllProducts, createProduct, updateProduct, deleteProduct
from middlewares.ProductMiddleware import productMiddleWare

UPLOAD_FOLDER = '/images'

def getProducts():

    products = getAllProducts()
    
    if products == None:
        return jsonify({"error": "An error occurred while getting all products"}), 500
    
    return products, 200
def getProduct(productId):
    
    product = getProductById(productId)
    
    if product == None:
        return jsonify({"error": "An error occurred while getting all products"}), 500
    
    return product, 200
def postProduct():

    productToCreate = productMiddleWare(request.get_json())

    if productToCreate == None:
        return jsonify({"error": "Invalid body"}), 400
        
    product = createProduct(productToCreate)
    
    if product == None:
        return jsonify({"error": "An error occurred while creating a product"}), 500
    
    return jsonify(product), 200
def putProduct(productId):
    
    productToUpdate = productMiddleWare(request.get_json())
    
    if productToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    product = updateProduct(productId, productToUpdate)
    
    if product == None:
        return jsonify({"error": "An error occurred while updating a product"}), 500
    
    return jsonify(product), 200
def dropProduct(productId):
        
        product = deleteProduct(productId)
        
        if product == None:
            return jsonify({"error": "An error occurred while deleting a product"}), 500
        
        return jsonify(product), 200