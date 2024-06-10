from flask import request, jsonify
from services.AdminUsersServices import getAdminUserById, getAllAdminUsers, createAdminUser, updateAdminUser, deleteAdminUser
from middlewares.AdminUserMiddleware import adminUserMiddleWare

def getAdminUsers():

    adminUsers = getAllAdminUsers()
    
    if adminUsers == None:
        return jsonify({"error": "An error occurred while getting all admin users "}), 500
    
    return adminUsers, 200

def getAdminUser(adminUserId):
    
    adminUser = getAdminUserById(adminUserId)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while getting admin user"}), 500
    
    return adminUser, 200

def postAdminUser():

    adminUserToCreate = adminUserMiddleWare(request.get_json())

    if adminUserToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    adminUser = createAdminUser(adminUserToCreate)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while creating a admin user"}), 500
    
    return jsonify(adminUser), 200

def putAdminUser(adminUserId):
    
    adminUserToUpdate = adminUserMiddleWare(request.get_json())
    
    if adminUserToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    adminUser = updateAdminUser(adminUserId, adminUserToUpdate)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while updating a admin user"}), 500
    
    return jsonify(adminUser), 200

def dropAdminUser(adminUserId):
        
        adminUser = deleteAdminUser(adminUserId)
        
        if adminUser == None:
            return jsonify({"error": "An error occurred while deleting a admin user"}), 500
        
        return jsonify(adminUser), 200