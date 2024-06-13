from database.database import db
from models.AdminUserModel import Admin
from werkzeug.security import generate_password_hash

def getAllAdminUsers():
    try:
        data = Admin.query.all()
        return [adminUser.toJSON() for adminUser in data]
    except Exception as e:
        print(str(e))
        return None
 
def getAdminUserById(adminUserId):
    try:
        data = Admin.query.filter_by(admID = adminUserId).first()
        return data.toJSON()
    except Exception as e:
        return None

def createAdminUser(data):
    try:
        adminUser = Admin(data.admEmail, data.admPassword)
        db.session.add(adminUser)
        db.session.commit()
        return {"message": "Admin user created"}
    except Exception as e:
        return None

def updateAdminUser(adminUserId, data):
    try:
        adminUser = Admin.query.filter_by(admID = adminUserId).first()
        
        newPass = generate_password_hash(data.admPassword)
        
        if adminUser.admEmail != data.admEmail:
            adminUser.admEmail = data.admEmail
            
        if adminUser.admPassword != newPass:
            adminUser.admPassword = newPass
        
        db.session.commit()
        return {"message": "Admin user updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteAdminUser(AdminUserId):
    try:
        adminUser = Admin.query.filter_by(admID = AdminUserId).first()
        db.session.delete(adminUser)
        db.session.commit()
        return {"message": "Admin user deleted"}
    except Exception as e:
        return None