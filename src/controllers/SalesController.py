from flask import request, jsonify
from middlewares.SalesMiddleware import SalesMiddleware
from services.SalesServices import  getAllSales, getSaleById, createSale, updateSale, deleteSale

def getSales():
    sales = getAllSales()
    
    if sales == None:
        return jsonify({"error": "Ocurrió un error al obtener todas las ventas"}), 500
    
    return sales, 200

def getSale(salId):
    sale = getSaleById(salId)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al obtener la venta"}), 500
    
    return sale, 200

def postSale():
    saleToCreate = SalesMiddleware(request.get_json())

    if saleToCreate == None:
        return jsonify({"error": "Cuerpo de solicitud inválido"}), 400
    
    sale = createSale(saleToCreate)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al crear la venta"}), 500
    
    return jsonify(sale), 200

def putSale(salId):
    saleToUpdate = salesMiddleWare(request.get_json())

    if saleToUpdate == None:
        return jsonify({"error": "Cuerpo de solicitud inválido"}), 400
    
    sale = updateSale(salId, saleToUpdate)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al actualizar la venta"}), 500
    
    return jsonify(sale), 200

def deleteSale(salId):
    sale = deleteSale(salId)
    
    if sale == None:
        return jsonify({"error": "Ocurrió un error al eliminar la venta"}), 500
    
    return jsonify(sale), 200
