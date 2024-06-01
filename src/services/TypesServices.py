from database.database import db
from models.ProductTypeModel import ProductType

def getAllProductTypes():
    try:
        data = ProductType.query.all()
        return [productType.toJSON() for productType in data]
    except Exception as e:
        print(str(e))
        return None

def getProductTypeById(productTypeID):
    try:
        data = ProductType.query.filter_by(ptID = productTypeID).first()
        return data.toJSON()
    except Exception as e:
        return None

def createProductType(data):
    try:
        productType = ProductType(data.ptName)
        db.session.add(productType)
        db.session.commit()
        return {"message": "Product type created"}
    except Exception as e:
        return None
    
def updateProductType(productTypeID, data):
    try:
        productType = ProductType.query.filter_by(ptID = productTypeID).first()
        
        if productType.ptName != data.ptName:
            productType.ptName = data.ptName

        db.session.commit()
        return {"message": "Product type updated"}
    except Exception as e:
        print(str(e))
        return None
    
def deleteProductType(productTypeID):
    try:
        productType = ProductType.query.filter_by(ptID = productTypeID).first()
        db.session.delete(productType)
        db.session.commit()
        return {"message": "Product type deleted"}
    except Exception as e:
        return None
