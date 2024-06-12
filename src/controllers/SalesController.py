from flask import request, jsonify
from middlewares.SalesMiddleware import postSalesMiddleWare, putSalesMiddleWare
from services.SalesServices import  getAllSales, getSaleById, createSale, updateSale, deleteSale
from middlewares.AuthMiddleware import verifyAdmin

def getSales():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    sales = getAllSales()
    
    if sales == None:
        return jsonify({"error": "Ocurrió un error al obtener todas las ventas"}), 500
    
    return sales, 200

def getSale(salId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    sale = getSaleById(salId)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al obtener la venta"}), 500
    
    return sale, 200

def postSale():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        salesToCreate = postSalesMiddleWare(request.get_json())

        if salesToCreate == None:
            return jsonify({"error": "Cuerpo de solicitud inválido"}), 400
        
        for saleToCreate in salesToCreate:
            sale = createSale(saleToCreate)
        
        return jsonify({"message": "sale was created"}), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error al crear la venta"}), 500

def putSale(salId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        salesToUpdate = putSalesMiddleWare(request.get_json(), salId)

        if salesToUpdate == None:
            return jsonify({"error": "Cuerpo de solicitud inválido"}), 400
        
        for saleToUpdate in salesToUpdate:
            sale = updateSale(saleToUpdate.salID, saleToUpdate)
        
        return jsonify(sale), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error al actualizar la venta"}), 500
    
def deleteSale(salId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    sale = deleteSale(salId)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al eliminar la venta"}), 500
    
    return jsonify(sale), 200
