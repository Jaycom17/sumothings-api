from models.ClientModel import Client
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from decouple import config

def authenticate(email, password):
    user = Client.query.filter_by(cliEmail=email).first()
    
    if user and check_password_hash(user.password, password):
        return user
    return None

def generate_token(user):
    payload = {
        'cliID': user.cliID,
        'exp': datetime.now() + timedelta(days=1)
    }
    
    return jwt.encode(payload, config('JWT_SECRET'), algorithm='HS256')

