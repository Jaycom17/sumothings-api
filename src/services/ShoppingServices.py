from sqlalchemy import func
from database.database import db
from models.ShoppingModel import Shopping

def getAllShoppings():
    try:
        # Primero, obtén los shoReceipt únicos
        unique_receipts = db.session.query(Shopping.shoReceipt).group_by(Shopping.shoReceipt).subquery()

        # Luego, une esto con la tabla original para obtener los detalles
        # Aquí, estoy asumiendo que quieres el primer registro para cada shoReceipt
        data = db.session.query(Shopping).join(
            unique_receipts,
            Shopping.shoReceipt == unique_receipts.c.shoReceipt
        ).all()

        print(data)

        return [shopping.toJSON() for shopping in data]
    except Exception as e:
        print(str(e))
        return None
    
def getShoppingById(shoppingId):
    try:
        data = Shopping.query.filter_by(shoID = shoppingId).first()
        return data.toJSON()
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
        shopping = Shopping.query.filter_by(shoID = shoppingId).first()
        db.session.delete(shopping)
        db.session.commit()
        return {"message": "Shopping deleted"}
    except Exception as e:
        return None