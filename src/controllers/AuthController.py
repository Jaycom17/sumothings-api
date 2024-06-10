from flask import request, jsonify, make_response
from services.AuthServices import authenticate, generate_token, authenticateAdmin, generate_token_admin
from middlewares.AuthMiddleware import verifyAdmin, verifyClient

def login():
    data = request.get_json()
    
    user = authenticate(data['cliEmail'], data['cliPassword'])
    
    if user:
        token = generate_token(user)
        
        resp = make_response(jsonify({"message": "Login successful"}))  
        
        resp.set_cookie('access_token', token, httponly=True, secure=False, samesite='Strict', max_age=86400)
        
        return resp, 200
    
    return jsonify({"message": "Invalid credentials"}), 401

def loginAdmin():
    data = request.get_json()
    
    user = authenticateAdmin(data['admEmail'], data['admPassword'])
    
    if user:
        token = generate_token_admin(user)
        
        resp = make_response(jsonify({"message": "Login successful"}))  
        
        resp.set_cookie('access_token', token, httponly=True, secure=False, samesite='Strict', max_age=86400)
        
        return resp, 200
    
    return jsonify({"message": "Invalid credentials"}), 401

def logout():
    resp = make_response(jsonify({"message": "Logout successful"}))
    
    resp.set_cookie('access_token', '', httponly=True, secure=False, samesite='Strict', max_age=0)
    
    return resp, 200

def validateAdmin():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, 'admID'):
        return jsonify({"isLoggedIn": True}), 200
    else:
        return jsonify({"isLoggedIn": False}), 401

def validateClient():
    verify = verifyClient(request)
    
    try:
        verify.cliID
    except AttributeError:
        return jsonify({"isLoggedIn": False}), 401
    
    return jsonify({"isLoggedIn": True}), 200
    