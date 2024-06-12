from sqlalchemy import func
from database.database import db
from models.ShoppingModel import Shopping
from models.ProductModel import Product
from models.DealerModel import Dealer

def getAllShoppings():
    try:
        receipts = Shopping.query.with_entities(Shopping.shoReceipt).distinct().all()
        
        data = []
        for receipt in receipts:
            shoppingToAdd = {}
            shoppingToAdd["shoReceipt"] = receipt[0]        
            products = Shopping.query.filter_by(shoReceipt = receipt[0]).all()
            shoppingToAdd["shoDate"] = products[0].shoDate
            shoppingToAdd["products"] = []
            for product in products:
                shoppingToAdd["products"].append(product.toJSON())
                productToAdd = Product.query.filter_by(proID = product.proID).first()
                shoppingToAdd["products"][-1]["proName"] = productToAdd.proName
                dealerToAdd = Dealer.query.filter_by(deaID = product.deaID).first()
                shoppingToAdd["deaName"] = dealerToAdd.deaFullName
                
            data.append(shoppingToAdd)
            
    
        return data
    except Exception as e:
        print(str(e))
        return None
    
def getShoppingById(shoppingId):
    try:
        data = Shopping.query.filter_by(shoReceipt = shoppingId).all()
        info = {}
        info["shoReceipt"] = shoppingId
        info["shoDate"] = data[0].shoDate
        dealerToAdd = Dealer.query.filter_by(deaID = data[0].deaID).first()
        info["deaName"] = dealerToAdd.deaFullName
        info["products"] = []
        for product in data:
            productToAdd = Product.query.filter_by(proID = product.proID).first()
            info["products"].append(product.toJSON())
            info["products"][-1]["proName"] = productToAdd.proName
        return info
    except Exception as e:
        return None

def createShopping(data):
    try:
        shopping = Shopping(data.proID, data.deaID, data.shoReceipt, data.shoDate, data.shoProductUnits, data.shoPrice, data.shoTaxes)
        db.session.add(shopping)
        db.session.commit()
        return {"message": "Shopping created"}
    except Exception as e:
        return None

def updateShopping(shoppingId, data):
    try:
        shopping = Shopping.query.filter_by(shoID = shoppingId).first()
        
        if shopping.proID != data.proID:
            shopping.proID = data.proID
            
        if shopping.deaID != data.deaID:
            shopping.deaID = data.deaID
            
        if shopping.shoReceipt != data.shoReceipt:
            shopping.shoReceipt = data.shoReceipt
            
        if shopping.shoDate != data.shoDate:
            shopping.shoDate = data.shoDate
            
        if shopping.shoProductUnits != data.shoProductUnits:
            shopping.shoProductUnits = data.shoProductUnits
            
        if shopping.shoPrice != data.shoPrice:
            shopping.shoPrice = data.shoPrice
            
        if shopping.shoTaxes != data.shoTaxes:
            shopping.shoTaxes = data.shoTaxes
        
        db.session.commit()
        return {"message": "Shopping updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteShopping(shoppingId):
    try:
        shoppings = Shopping.query.filter_by(shoReceipt = shoppingId).all()
        
        for shopping in shoppings:
            db.session.delete(shopping)
            db.session.commit()
        
        return {"message": "Shopping deleted"}
    except Exception as e:
        return None