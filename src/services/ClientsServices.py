from database.database import db
from models.ClientModel import Client

def getAllClients():
    try:
        data = Client.query.all()
        return [client.toJSON() for client in data]
    except Exception as e:
        print(str(e))
        return None
 
def getClientById(cliId):
    try:
        data = Client.query.filter_by(cliID = cliId).first()
        return data.toJSON()
    except Exception as e:
        return None

def createClient(data):
    try:
        client = Client(data.cliFullName, data.cliEmail, data.cliPassword, data.cliPhone, data.cliAddress, data.cliNIT, data.cliCompanyName, data.cliCity, data.cliPostalCode, data.cliCedula)
        db.session.add(client)
        db.session.commit()
        return {"message": "Client created"}
    except Exception as e:
        return None

def updateClient(cliId, data):
    try:
        client = Client.query.filter_by(cliID = cliId).first()

        if client is None:
            return {"error": "Client not found with ID {}".format(cliId)}
        
        if data is None:
            return {"error": "Invalid data provided"}
            
        if client.cliFullName != data.cliFullName:
            client.cliFullName = data.cliFullName
            
        if client.cliEmail != data.cliEmail:
            client.cliEmail = data.cliEmail
                        
        if client.cliPassword != data.cliPassword:
            client.cliPassword = data.cliPassword
                        
        if client.cliPhone != data.cliPhone:
            client.cliPhone = data.cliPhone
                        
        if client.cliAddress != data.cliAddress:
            client.cliAddress = data.cliAddress
                        
        if client.cliNIT != data.cliNIT:
            client.cliNIT = data.cliNIT
                        
        if client.cliCompanyName != data.cliCompanyName:
            client.cliCompanyName = data.cliCompanyName
                        
        if client.cliCity != data.cliCity:
            client.cliCity = data.cliCity
                        
        if client.cliPostalCode != data.cliPostalCode:
            client.cliPostalCode = data.cliPostalCode
                        
        if client.cliCedula != data.cliCedula:
            client.cliCedula = data.cliCedula
        
        db.session.commit()
        return {"message": "Client updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteClient(cliId):
    try:
        client = Client.query.filter_by(cliID = cliId).first()
        db.session.delete(client)
        db.session.commit()
        return {"message": "Client deleted"}
    except Exception as e:
        return None