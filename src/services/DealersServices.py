from database.database import db
from models.DealerModel import Dealer

def getAllDealers():
    try:
        data = Dealer.query.all()
        return [dealer.toJSON() for dealer in data]
    except Exception as e:
        print(str(e))
        return None
 
def getDealerById(dealerId):
    try:
        data = Dealer.query.filter_by(deaID = dealerId).first()
        return data.toJSON()
    except Exception as e:
        return None

def createDealer(data):
    try:
        dealer = Dealer(data.deaFullName, data.deaEmail, data.deaPhone, data.deaCedula)
        db.session.add(dealer)
        db.session.commit()
        return {"message": "Dealer created"}
    except Exception as e:
        return None

def updateDealer(dealerId, data):
    try:
        dealer = Dealer.query.filter_by(deaID = dealerId).first()
        
        if dealer.deaFullName != data.deaFullName:
            dealer.deaFullName = data.deaFullName
            
        if dealer.deaEmail != data.deaEmail:
            dealer.deaEmail = data.deaEmail
            
        if dealer.deaPhone != data.deaPhone:
            dealer.deaPhone = data.deaPhone
            
        if dealer.deaCedula != data.deaCedula:
            dealer.deaCedula = data.deaCedula
        
        db.session.commit()
        return {"message": "Dealer updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteDealer(dealerId):
    try:
        dealer = Dealer.query.filter_by(deaID = dealerId).first()
        db.session.delete(dealer)
        db.session.commit()
        return {"message": "Dealer deleted"}
    except Exception as e:
        return None
