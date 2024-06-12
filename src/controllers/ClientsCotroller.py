from flask import request, jsonify
from services.ClientsServices import getAllClients, getClientById, createClient, updateClient, deleteClient
from middlewares.ClientMiddleware import clientMiddleWare
from middlewares.AuthMiddleware import verifyAdmin

def getClients():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401

    clients = getAllClients()
    
    if clients == None:
        return jsonify({"error": "An error occurred while getting all clients "}), 500
    
    return clients, 200

def getClient(cliId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    client = getClientById(cliId)
    
    if client == None:
        return jsonify({"error": "An error occurred while getting client"}), 500
    
    return client, 200

def postClient():

    clientToCreate = clientMiddleWare(request.get_json())

    if clientToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    client = createClient(clientToCreate)
    
    if client == None:
        return jsonify({"error": "An error occurred while creating a client"}), 500
    
    return jsonify(client), 200

def putClient(cliId):
    
    clientToUpdate = clientMiddleWare(request.get_json())
    
    if clientToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    client = updateClient(cliId, clientToUpdate)
    
    if client == None:
        return jsonify({"error": "An error occurred while updating a client"}), 500
    
    return jsonify(client), 200

def dropClient(cliId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
        
    client = deleteClient(cliId)
    
    if client == None:
        return jsonify({"error": "An error occurred while deleting a client"}), 500
    
    return jsonify(client), 200