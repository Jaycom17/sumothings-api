from database.database import db
from models.ProductTypeModel import ProductType
import uuid

class ProductModel:
    def __init__(self, proName: str, proStock: int, proHeight: float, proLength: float, proWidth: float, proWeight: float,proBuyPrice: float,  proSellPrice: float, proMinStock: int, proMaxStock: int, proDescription: str, proTypeID: str):
        self.proName = proName
        self.proStock = proStock
        self.proHeight = proHeight
        self.proLength = proLength
        self.proBuyPrice = proBuyPrice
        self.proWidth = proWidth
        self.proWeight = proWeight
        self.proSellPrice = proSellPrice
        self.proMinStock = proMinStock
        self.proMaxStock = proMaxStock
        self.proDescription = proDescription
        self.proImage = None
        self.proTypeID = proTypeID
        self.proImage = None

class Product(db.Model):
    __tablename__ = 'product'
    proID = db.Column(db.String(255), primary_key=True)
    proName = db.Column(db.String(128), nullable=False, unique=True)
    proStock = db.Column(db.Integer, nullable=False)
    proHeight = db.Column(db.Float, nullable=False)
    proLength = db.Column(db.Float, nullable=False)
    proBuyPrice = db.Column(db.Float, nullable=False)
    proWidth = db.Column(db.Float, nullable=False)
    proWeight = db.Column(db.Float, nullable=False)
    proSellPrice = db.Column(db.Float, nullable=False)
    proMinStock = db.Column(db.Integer, nullable=False)
    proMaxStock = db.Column(db.Integer, nullable=False)
    proDescription = db.Column(db.Text, nullable=False)
    proImage = db.Column(db.String(255), nullable=False)
    proTypeID = db.Column(db.String(255), db.ForeignKey('producttype.ptID'), nullable=False)

    
    def __init__(self, proName: str, proStock: int, proHeight: float, proLength: float, proWidth: float,proBuyPrice: float, proWeight: float, proSellPrice: float, proMinStock: int, proMaxStock: int, proDescription: str, proImage: str, proTypeID: str):
        self.proID = uuid.uuid4().hex
        self.proName = proName
        self.proStock = proStock
        self.proHeight = proHeight
        self.proLength = proLength
        self.proWidth = proWidth
        self.proBuyPrice = proBuyPrice
        self.proWeight = proWeight
        self.proSellPrice = proSellPrice
        self.proMinStock = proMinStock
        self.proMaxStock = proMaxStock
        self.proDescription = proDescription
        self.proImage = proImage
        self.proTypeID = proTypeID
        
    def toJSON(self):
        return {
            "proID": self.proID,
            "proName": self.proName,
            "proStock": self.proStock,
            "proHeight": self.proHeight,
            "proLength": self.proLength,
            "proBuyPrice": self.proBuyPrice,
            "proWidth": self.proWidth,
            "proWeight": self.proWeight,
            "proSellPrice": self.proSellPrice,
            "proMinStock": self.proMinStock,
            "proMaxStock": self.proMaxStock,
            "proDescription": self.proDescription,
            "proImage": self.proImage,
            "proTypeID": self.proTypeID
        }