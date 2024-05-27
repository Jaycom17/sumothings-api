from database.database import db
import uuid
from datetime import datetime
from models.SalesModel import Sales

def getAllSales():
    try:
        data = Sales.query.all()
        return [sales.toJSON() for sales in data]
    except Exception as e:
        print(str(e))
        return None
    
def getSaleById(saleId):
    try:
        data = Sales.query.filter_by(salID=saleId).first()
        return data.toJSON()
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
        sales = Sales.query.filter_by(salID=saleId).first()
        
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
