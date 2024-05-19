from database.database import db
import uuid

class ProductModel:
    def __init__(self, proName: str, proStock: int, proHeight: float, proLength: float, proWidth: float, proWeight: float, proCostPrice: float, proSellingPrice: float, proMinStock: int, proMaxStock: int, proDescription: str, proImage: str, typeID: str):
        self.proName = proName
        self.proStock = proStock
        self.proHeight = proHeight
        self.proLength = proLength
        self.proWidth = proWidth
        self.proWeight = proWeight
        self.proCostPrice = proCostPrice
        self.proSellingPrice = proSellingPrice
        self.proMinStock = proMinStock
        self.proMaxStock = proMaxStock
        self.proDescription = proDescription
        self.proImage = proImage
        self.typeID = typeID

class Product(db.Model):
    proID = db.Column(db.String(255), primary_key=True)
    proName = db.Column(db.String(128), nullable=False, unique=True)
    proStock = db.Column(db.Integer, nullable=False)
    proHeight = db.Column(db.Float, nullable=False)
    proLength = db.Column(db.Float, nullable=False)
    proWidth = db.Column(db.Float, nullable=False)
    proWeight = db.Column(db.Float, nullable=False)
    proCostPrice = db.Column(db.Float, nullable=False)
    proSellingPrice = db.Column(db.Float, nullable=False)
    proMinStock = db.Column(db.Integer, nullable=False)
    proMaxStock = db.Column(db.Integer, nullable=False)
    proDescription = db.Column(db.Text, nullable=False)
    proImage = db.Column(db.String(255), nullable=False)
    typeID = db.Column(db.String(255), db.ForeignKey('product_type.typeID'), nullable=False)
    
    def __init__(self, proName: str, proStock: int, proHeight: float, proLength: float, proWidth: float, proWeight: float, proCostPrice: float, proSellingPrice: float, proMinStock: int, proMaxStock: int, proDescription: str, proImage: str, typeID: str):
        self.proID = uuid.uuid4().hex
        self.proName = proName
        self.proStock = proStock
        self.proHeight = proHeight
        self.proLength = proLength
        self.proWidth = proWidth
        self.proWeight = proWeight
        self.proCostPrice = proCostPrice
        self.proSellingPrice = proSellingPrice
        self.proMinStock = proMinStock
        self.proMaxStock = proMaxStock
        self.proDescription = proDescription
        self.proImage = proImage
        self.typeID = typeID
        
    def toJSON(self):
        return {
            "proID": self.proID,
            "proName": self.proName,
            "proStock": self.proStock,
            "proHeight": self.proHeight,
            "proLength": self.proLength,
            "proWidth": self.proWidth,
            "proWeight": self.proWeight,
            "proCostPrice": self.proCostPrice,
            "proSellingPrice": self.proSellingPrice,
            "proMinStock": self.proMinStock,
            "proMaxStock": self.proMaxStock,
            "proDescription": self.proDescription,
            "proImage": self.proImage,
            "typeID": self.typeID
        }