from flask import request, jsonify
from services.ProductsServices import getProductById, getAllProducts, createProduct, updateProduct, deleteProduct, allowed_file
from middlewares.ProductMiddleware import productMiddleWare
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import current_app as app


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
    print(request.get_json())

    productToCreate = productMiddleWare(request.get_json())

    if productToCreate == None:
        return jsonify({"error": "Invalid body"}), 400
    if 'file' not in request.files:
        flash('No file part')
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    productToCreate.proImage = filename
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

def download_file(imgName):
    return send_from_directory(app.config["UPLOAD_FOLDER"], imgName)
   