from flask import request, jsonify
from services.AdminUsersServices import getAdminUserById, getAllAdminUsers, createAdminUser, updateAdminUser, deleteAdminUser
from middlewares.AdminUserMiddleware import adminUserMiddleWare
from middlewares.AuthMiddleware import verifyAdmin

def getAdminUsers():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401

    adminUsers = getAllAdminUsers()
    
    if adminUsers == None:
        return jsonify({"error": "An error occurred while getting all admin users "}), 500
    
    return adminUsers, 200

def getAdminUser(adminUserId):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    adminUser = getAdminUserById(adminUserId)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while getting admin user"}), 500
    
    return adminUser, 200

def postAdminUser():
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401

    adminUserToCreate = adminUserMiddleWare(request.get_json())

    if adminUserToCreate == None:
        return jsonify({"error": "Invalid body"}), 400

    adminUser = createAdminUser(adminUserToCreate)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while creating a admin user"}), 500
    
    return jsonify(adminUser), 200

def putAdminUser():
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
    
    adminUserToUpdate = adminUserMiddleWare(request.get_json())
    
    if adminUserToUpdate == None:
        return jsonify({"error": "Invalid body"}), 400
    
    adminUser = updateAdminUser(verify.admID, adminUserToUpdate)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while updating a admin user"}), 500
    
    return jsonify(adminUser), 200

def dropAdminUser(admID):
    
    verify = verifyAdmin(request)
    
    if hasattr(verify, "admID") == False:
        return jsonify({"error": "Unauthorized"}), 401
        
    adminUser = deleteAdminUser(admID)
    
    if adminUser == None:
        return jsonify({"error": "An error occurred while deleting a admin user"}), 500
    
    return jsonify(adminUser), 200