from database.database import db
import uuid

class ProductTypeModel:
    def __init__(self, typeName: str):
        self.typeName = typeName

class ProductType(db.Model):
    typeID = db.Column(db.String(255), primary_key=True)
    typeName = db.Column(db.String(128), nullable=False, unique=True)
    
    def __init__(self, typeName: str):
        self.typeID = uuid.uuid4().hex
        self.typeName = typeName
        
    def toJSON(self):
        return {
            "typeID": self.typeID,
            "typeName": self.typeName
        }