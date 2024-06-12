from database.database import db
import uuid
from datetime import datetime
from models.SalesModel import Sales
from models.ProductModel import Product
from models.ClientModel import Client

def getAllSales():
    try:
        receipts = Sales.query.with_entities(Sales.salReceipt).distinct().all()
        
        data = []
        for receipt in receipts:
            saleToAdd = {}
            saleToAdd["salReceipt"] = receipt[0]        
            products = Sales.query.filter_by(salReceipt = receipt[0]).all()
            saleToAdd["salDate"] = products[0].salDate
            saleToAdd["products"] = []
            for product in products:
                saleToAdd["products"].append(product.toJSON())
                productToAdd = Product.query.filter_by(proID = product.proID).first()
                saleToAdd["products"][-1]["proName"] = productToAdd.proName
                clientToAdd = Client.query.filter_by(cliID = product.cliID).first()
                saleToAdd["cliName"] = clientToAdd.cliFullName
                
            data.append(saleToAdd)
            
    
        return data
    except Exception as e:
        print(str(e))
        return None
    
def getSaleById(saleId):
    try:
        data = Sales.query.filter_by(salReceipt = saleId).all()
        info = {}
        info["salReceipt"] = saleId
        info["salDate"] = data[0].salDate
        clientToAdd = Client.query.filter_by(cliID = data[0].cliID).first()
        info["cliName"] = clientToAdd.cliFullName
        info["products"] = []
        for product in data:
            productToAdd = Product.query.filter_by(proID = product.proID).first()
            info["products"].append(product.toJSON())
            info["products"][-1]["proName"] = productToAdd.proName
        return info
    except Exception as e:
        return None

def createSale(data):
    try:
        sales = Sales(
            data.proID,
            data.cliID,
            data.salReceipt,
            data.salDate,
            data.salProductUnits,
            data.salPrice,
            data.salTaxes
        )
        db.session.add(sales)
        db.session.commit()
        return {"message": "Sale created"}
    except Exception as e:
        return None

def updateSale(saleId, data):
    try:
        sales = Sales.query.filter_by(salID = saleId).first()
        
        if sales.proID != data.proID:
            sales.proID = data.proID
            
        if sales.cliID != data.cliID:
            sales.cliID = data.cliID
            
        if sales.salReceipt != data.salReceipt:
            sales.salReceipt = data.salReceipt
            
        if sales.salDate != data.salDate:
            sales.salDate = data.salDate
            
        if sales.salProductUnits != data.salProductUnits:
            sales.salProductUnits = data.salProductUnits
            
        if sales.salPrice != data.salPrice:
            sales.salPrice = data.salPrice
            
        if sales.salTaxes != data.salTaxes:
            sales.salTaxes = data.salTaxes
        
        db.session.commit()
        return {"message": "Sale updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteSale(saleId):
    try:
        sales = Sales.query.filter_by(salID=saleId).first()
        db.session.delete(sales)
        db.session.commit()
        return {"message": "Sale deleted"}
    except Exception as e:
        return None
