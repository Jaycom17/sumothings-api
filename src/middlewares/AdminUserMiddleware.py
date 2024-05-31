from models.AdminUserModel import AdminUserModel

def adminUserMiddleWare(adminUser):
    try:
        return AdminUserModel(adminUser["admEmail"], adminUser["admPassword"])
    except KeyError as e:
        return None