from flask import request, jsonify
from services.AuthServices import authenticate, generate_token

def login():
    data = request.get_json()
    user = authenticate(data['cliEmail'], data['cliPassword'])
    if user:
        token = generate_token(user)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401