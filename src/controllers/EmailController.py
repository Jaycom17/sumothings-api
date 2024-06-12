from flask import request, jsonify
from services.EmailService import send_email
from middlewares.EmailMiddleware import emailMiddleware

def sendEmail():
    data = request.get_json()
    
    information = emailMiddleware(data)
    
    if information == None:
        return jsonify({"message": "Invalid body"}), 400
    
    if send_email(information['subject'], information['body'], information['email']):
        return jsonify({"message": "Email sent"}), 200
    
    return jsonify({"message": "An error occurred while sending email"}), 500