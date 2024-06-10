from flask import jsonify
import jwt
from decouple import config
from models.ClientModel import Client
from models.AdminUserModel import Admin

def verifyClient(request):
    token = request.cookies.get('access_token')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401
    try:
        data = jwt.decode(token, config('JWT_SECRET'), algorithms=['HS256'])
        
        current_user = Client.query.filter_by(cliID=data['cliID']).first()
        
        if current_user == None:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return current_user
        
    except:
        return jsonify({'message': 'Token is invalid!'}), 401

def verifyAdmin(request):
    token = request.cookies.get('access_token')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401
    try:
        data = jwt.decode(token, config('JWT_SECRET'), algorithms=['HS256'])
        
        current_user = Admin.query.filter_by(admID=data['admID']).first()
        
        if current_user == None:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return current_user
        
    except:
        return jsonify({'message': 'Token is invalid!'}), 401