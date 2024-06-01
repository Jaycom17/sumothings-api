from database.database import db
import uuid

class ProductTypeModel:
    def __init__(self, ptName: str):
        self.ptName = ptName

class ProductType(db.Model):
    __tablename__ = 'producttype'
    ptID = db.Column(db.String(255), primary_key=True)
    ptName = db.Column(db.String(128), nullable=False, unique=True)
    products = db.relationship('Product', backref='producttype', lazy=True)    
    
    def __init__(self, ptName: str):
        self.ptID = uuid.uuid4().hex
        self.ptName = ptName
        
    def toJSON(self):
        return {
            "ptID": self.ptID,
            "ptName": self.ptName
        }