from database.database import db
import uuid

class ShoppingModel:
    def __init__(self, proID: str, deaID: str, shoReceipt: str, shoDate: str, shoProductUnits: int, shoPrice: float, shoTaxes: float):
        self.proID = proID
        self.deaID = deaID
        self.shoReceipt = shoReceipt
        self.shoDate = shoDate
        self.shoProductUnits = shoProductUnits
        self.shoPrice = shoPrice
        self.shoTaxes = shoTaxes

class Shopping(db.Model):
    shoID = db.Column(db.String(255), primary_key=True)
    proID = db.Column(db.String(255), db.ForeignKey('product.proID'), nullable=False)
    deaID = db.Column(db.String(255), db.ForeignKey('dealer.deaID'), nullable=False)
    shoReceipt = db.Column(db.String(255), nullable=False)
    shoDate = db.Column(db.DateTime, nullable=False)
    shoProductUnits = db.Column(db.Integer, nullable=False)
    shoPrice = db.Column(db.Float, nullable=False)
    shoTaxes = db.Column(db.Float, nullable=False)
    
    def __init__(self, proID: str, deaID: str, shoReceipt: str, shoDate: str, shoProductUnits: int, shoPrice: float, shoTaxes: float):
        self.shoID = uuid.uuid4().hex
        self.proID = proID
        self.deaID = deaID
        self.shoReceipt = shoReceipt
        self.shoDate = shoDate
        self.shoProductUnits = shoProductUnits
        self.shoPrice = shoPrice
        self.shoTaxes = shoTaxes
        
    def toJSON(self):
        return {
            "shoID": self.shoID,
            "proID": self.proID,
            "deaID": self.deaID,
            "shoReceipt": self.shoReceipt,
            "shoDate": self.shoDate,
            "shoProductUnits": self.shoProductUnits,
            "shoPrice": self.shoPrice,
            "shoTaxes": self.shoTaxes
        }