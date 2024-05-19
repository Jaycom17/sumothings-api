from database.database import get_db

def getAllDealers():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Dealer")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(e)
        return {"error": "Error on get all dealers"}
 
def getDealerById(dealerId):
    return f"Dealer with id {dealerId}"

def createDealer(data):
    return data.toJSON()

def updateDealer(dealerId, data):
    return f"Dealer with id {dealerId} updated"

def deleteDealer(dealerId):
    return f"Dealer with id {dealerId} deleted"
