from models.ClientModel import Client
from models.AdminUserModel import Admin
import jwt
from datetime import datetime, timedelta
from decouple import config

def authenticate(email, password):
    user = Client.query.filter_by(cliEmail = email).first()
    
    if user and user.check_password(password):
        return user
    return None
    
def authenticateAdmin(email, password):
    user = Admin.query.filter_by(admEmail = email).first()
    
    if user and user.check_password(password):
        return user
    return None

def generate_token(user):
    payload = {
        'cliID': user.cliID,
        'exp': datetime.now() + timedelta(days=1)
    }
    
    return jwt.encode(payload, config('JWT_SECRET'), algorithm='HS256')

def generate_token_admin(user):
    payload = {
        'admID': user.admID,
        'exp': datetime.now() + timedelta(days=1)
    }
    
    return jwt.encode(payload, config('JWT_SECRET'), algorithm='HS256')

