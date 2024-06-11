from flask import request, jsonify
from services.DealersServices import getDealerById, getAllDealers, createDealer, updateDealer, deleteDealer
from middlewares.DealerMiddleware import dealerMiddleWare
from middlewares.AuthMiddleware import verifyAdmin

def getDealers():
    
    verify = verifyAdmin(request)

    try:
        verify.admID
    except AttributeError as error:
        return verify
    
    dealers = getAllDealers()
    
    if dealers == None:
        return jsonify({"error": "An error occurred while getting all dealers"}), 500
    
    return dealers, 200

def getDealer(dealerId):
    
    dealer = getDealerById(dealerId)
    
    if dealer == None:
        return jsonify({"error": "An error occurred while getting all dealers"}), 500
    
    return dealer, 200

def postDealer():

    dealerToCreate = dealerMiddleWare(request.get_json())

    if dealerToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    dealer = createDealer(dealerToCreate)
    
    if dealer == None:
        return jsonify({"error": "An error occurred while creating a dealer"}), 500
    
    return jsonify(dealer), 200

def putDealer(dealerId):
    
    dealerToUpdate = dealerMiddleWare(request.get_json())
    
    if dealerToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    dealer = updateDealer(dealerId, dealerToUpdate)
    
    if dealer == None:
        return jsonify({"error": "An error occurred while updating a dealer"}), 500
    
    return jsonify(dealer), 200

def dropDealer(dealerId):
        
        dealer = deleteDealer(dealerId)
        
        if dealer == None:
            return jsonify({"error": "An error occurred while deleting a dealer"}), 500
        
        return jsonify(dealer), 200

