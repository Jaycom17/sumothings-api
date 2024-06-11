from database.database import db
from models.ProductModel import Product
from models.ProductTypeModel import ProductType
import os


def getAllProducts():
    try:
        data = db.session.query(Product, ProductType)\
                  .join(ProductType, Product.proTypeID == ProductType.ptID)\
                  .all()
                  
        dataJson = []          
        for product in data:
            dataDict = {}
            dataDict["proID"] = product.Product.proID
            dataDict["proName"] = product.Product.proName
            dataDict["proStock"] = product.Product.proStock
            dataDict["proHeight"] = product.Product.proHeight
            dataDict["proWidth"] = product.Product.proWidth
            dataDict["proLength"] = product.Product.proLength
            dataDict["proWeight"] = product.Product.proWeight
            dataDict["proBuyPrice"] = product.Product.proBuyPrice
            dataDict["proSellPrice"] = product.Product.proSellPrice
            dataDict["proMinStock"] = product.Product.proMinStock
            dataDict["proMaxStock"] = product.Product.proMaxStock
            dataDict["proDescription"] = product.Product.proDescription
            dataDict["proImage"] = product.Product.proImage
            dataDict["proTypeID"] = product.ProductType.ptName
            dataJson.append(dataDict)
            
        
        return dataJson 
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
        product = Product(data.proName, data.proStock, data.proHeight, data.proLength, data.proWidth, data.proBuyPrice, data.proWeight, data.proSellPrice, data.proMinStock, data.proMaxStock, data.proDescription, data.proImage, data.proTypeID)
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
        os.remove(os.path.join("images/",product.proImage.split("/")[4]))
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}
    except Exception as e:
        print(str(e))
        return None

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}                        
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
