from database.database import db
import uuid
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Client():
    def __init__(self, cliID, cliFullName, cliEmail, cliPassword, cliPhone, cliAddress, cliNIT, cliCompanyName, cliCity, cliPostalCode, cliCedula):
        self.cliID = cliID
        self.cliFullName = cliFullName
        self.cliEmail = cliEmail
        self.cliPassword = cliPassword
        self.cliPhone = cliPhone
        self.cliAddress = cliAddress
        self.cliNIT = cliNIT
        self.cliCompanyName = cliCompanyName
        self.cliCity = cliCity
        self.cliPostalCode = cliPostalCode
        self.cliCedula = cliCedula

class Client(db.Model):
    __tablename__ = 'client'

    cliID = db.Column(db.String(128), primary_key=True)
    cliFullName = db.Column(db.String(128), nullable=True)
    cliEmail = db.Column(db.String(128), unique=True, nullable=True)
    cliPassword = db.Column(db.String(255), nullable=True)
    cliPhone = db.Column(db.String(15), unique=True, nullable=True)
    cliAddress = db.Column(db.String(128), nullable=True)
    cliNIT = db.Column(db.String(255), unique=True, nullable=True)
    cliCompanyName = db.Column(db.String(128), nullable=True)
    cliCity = db.Column(db.String(128), nullable=True)
    cliPostalCode = db.Column(db.String(64), nullable=True)
    cliCedula = db.Column(db.String(32), unique=True, nullable=True)

    def __init__(self, cliFullName, cliEmail, cliPassword, cliPhone, cliAddress, cliNIT, cliCompanyName, cliCity, cliPostalCode, cliCedula):
        self.cliID = uuid.uuid4().hex
        self.cliFullName = cliFullName
        self.cliEmail = cliEmail
        self.cliPassword = bcrypt.generate_password_hash(cliPassword).decode('utf-8')
        self.cliPhone = cliPhone
        self.cliAddress = cliAddress
        self.cliNIT = cliNIT
        self.cliCompanyName = cliCompanyName
        self.cliCity = cliCity
        self.cliPostalCode = cliPostalCode
        self.cliCedula = cliCedula
    
    def toJSON(self):
        return {
            "cliID": self.cliID,
            "cliFullName": self.cliFullName,
            "cliEmail": self.cliEmail,
            "cliPhone": self.cliPhone,
            "cliAddress": self.cliAddress,
            "cliNIT": self.cliNIT,
            "cliCompanyName": self.cliCompanyName,
            "cliCity": self.cliCity,
            "cliPostalCode": self.cliPostalCode,
            "cliCedula": self.cliCedula
        }
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.cliPassword, password)