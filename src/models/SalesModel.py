from database.database import db
import uuid
from datetime import datetime
from models.ClientModel import Client

class SalesModel:
    def __init__(self, proID: str, cliID: str, salReceipt: str, salDate: datetime, salProductUnits: int, salPrice: float, salTaxes: float):
        self.proID = proID
        self.cliID = cliID
        self.salReceipt = salReceipt
        self.salDate = salDate
        self.salProductUnits = salProductUnits
        self.salPrice = salPrice
        self.salTaxes = salTaxes

class Sales(db.Model):
    __tablename__ = 'sales'
    
    salID = db.Column(db.String(128), primary_key=True)
    proID = db.Column(db.String(128), db.ForeignKey('product.proID'), nullable=False)
    cliID = db.Column(db.String(128), db.ForeignKey('client.cliID'), nullable=False)
    salReceipt = db.Column(db.String(255), nullable=False)
    salDate = db.Column(db.Date, nullable=False, default=datetime.utcnow().date)
    salProductUnits = db.Column(db.Integer, nullable=False)
    salPrice = db.Column(db.Numeric(14, 2), nullable=False)
    salTaxes = db.Column(db.Numeric(14, 2), nullable=False)
    
    def __init__(self, proID: str, cliID: str, salReceipt: str, salDate: datetime, salProductUnits: int, salPrice: float, salTaxes: float):
        self.salID = uuid.uuid4().hex
        self.proID = proID
        self.cliID = cliID
        self.salReceipt = salReceipt
        self.salDate = salDate
        self.salProductUnits = salProductUnits
        self.salPrice = salPrice
        self.salTaxes = salTaxes
        
    def toJSON(self):
        return {
            "salID": self.salID,
            "proID": self.proID,
            "cliID": self.cliID,
            "salReceipt": self.salReceipt,
            "salDate": self.salDate.isoformat(),
            "salProductUnits": self.salProductUnits,
            "salPrice": float(self.salPrice),
            "salTaxes": float(self.salTaxes)
        }
