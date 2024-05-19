from flask import request, jsonify
from services.DealersServices import getDealerById, getAllDealers, createDealer, updateDealer, deleteDealer
from middlewares.DealerMiddelware import dealerMiddleWare

def getDealers():

    dealers = getAllDealers()

    return getAllDealers(), 200

def getDealer(dealerId):
    return getDealerById(dealerId), 200

def postDealer():

    dealer = dealerMiddleWare(request.get_json())

    if dealer == None:
        return jsonify({"error": "Invalid body"}), 400

    return createDealer(dealer), 200

def putDealer(dealerId):
    return updateDealer(dealerId, ""), 200

def dropDealer(dealerId):
    return deleteDealer(dealerId), 200

