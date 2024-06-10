from database.database import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class AdminUserModel:
    def __init__(self, admEmail:str, admPassword:str):
        self.admEmail = admEmail
        self.admPassword = admPassword

class Admin(db.Model):
    admID = db.Column(db.String(255), primary_key=True)
    admEmail = db.Column(db.String(228), nullable=False, unique=True)
    admPassword = db.Column(db.String(64), nullable=False)
    
    def __init__(self, admEmail:str, admPassword:str):
        self.admID = uuid.uuid4().hex
        self.admEmail = admEmail
        self.admPassword = generate_password_hash(admPassword)
        
    def toJSON(self):
        return {
            "admID": self.admID, 
            "admEmail": self.admEmail
        }
        
    def check_password(self, password):
        return check_password_hash(self.admPassword, password)