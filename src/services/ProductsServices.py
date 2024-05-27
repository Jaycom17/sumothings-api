from database.database import db
from models.ProductModel import Product

def getAllProducts():
    try:
        data = Product.query.all()
        return [product.toJSON() for product in data]
    except Exception as e:
        print(str(e))
        return None
    
    
def getProductById(productID):
    try:
        data = Product.query.filter_by(proID = productID).first()
        return data.toJSON()
    except Exception as e:
        return None

def createProduct(data):
    try:
        product = Product(data.proName, data.proStock, data.proHeight, data.proWidth, data.proLength, data.proWeight, data.proBuyPrice, data.proSellPrice, data.proMinStock, data.proMaxStock, data.proDescription, data.proImage, data.proTypeID)
        db.session.add(product)
        db.session.commit()
        return {"message": "Product created"}
    except Exception as e:
        print(str(e))
        return None
    
def updateProduct(productID,data):
    try:
        product = Product.query.filter_by(proID = productID).first()
        
        if product.proName != data.proName:
            product.proName = data.proName
            
        if product.proStock != data.proStock:
            product.proStock = data.proStock
            
        if product.proHeight != data.proHeight:
            product.proHeight = data.proHeight
            
        if product.proWidth != data.proWidth:
            product.proWidth = data.proWidth
            
        if product.proLength != data.proLength:
            product.proLength = data.proLength
            
        if product.proWeight != data.proWeight:
            product.proWeight = data.proWeight
            
        if product.proBuyPrice != data.proBuyPrice:
            product.proBuyPrice = data.proBuyPrice
            
        if product.proSellPrice != data.proSellPrice:
            product.proSellPrice = data.proSellPrice
            
        if product.proMinStock != data.proMinStock:
            product.proMinStock = data.proMinStock
            
        if product.proMaxStock != data.proMaxStock:
            product.proMaxStock = data.proMaxStock
            
        if product.proDescription != data.proDescription:
            product.proDescription = data.proDescription
            
        if product.proImage != data.proImage:
            product.proImage = data.proImage
            
        if product.proTypeID != data.proTypeID:
            product.proTypeID = data.proTypeID
        
        db.session.commit()
        return {"message": "Product updated"}
    except Exception as e:
        return None
def deleteProduct(productID):
    try:
        product = Product.query.filter_by(proID = productID).first()
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}
    except Exception as e:
        return None
                            