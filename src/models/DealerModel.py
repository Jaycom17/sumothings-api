from database.database import db
import uuid

class DealerModel:
    def __init__(self, deaFullName: str, deaEmail:str, deaPhone:str, deaCedula:str):
        self.deaFullName = deaFullName
        self.deaEmail = deaEmail
        self.deaPhone = deaPhone
        self.deaCedula = deaCedula

class Dealer(db.Model):
    __tablename__ = 'dealer'
    deaID = db.Column(db.String(255), primary_key=True)
    deaFullName = db.Column(db.String(128), nullable=False)
    deaEmail = db.Column(db.String(228), nullable=False, unique=True)
    deaPhone = db.Column(db.String(64), nullable=False)
    deaCedula = db.Column(db.String(64), nullable=False, unique=True)
    shoppings = db.relationship('Shopping', backref='dealer', lazy=True)
    
    def __init__(self, deaFullName: str, deaEmail:str, deaPhone:str, deaCedula:str):
        self.deaID = uuid.uuid4().hex
        self.deaFullName = deaFullName
        self.deaEmail = deaEmail
        self.deaPhone = deaPhone
        self.deaCedula = deaCedula
        
    def toJSON(self):
        return {
            "deaID": self.deaID, 
            "deaFullName": self.deaFullName,
            "deaEmail": self.deaEmail,
            "deaPhone": self.deaPhone,
            "deaCedula": self.deaCedula
        }