import pymongo

def create_user(client, username, password, email=None):
    db = client["mydatabase"]
    users = db["users"]
    user = {"username": username, "password": password, "email": email, "is_active": True, "is_staff": False}
    result = users.insert_one(user)
    return result.inserted_id

def create_superuser(client, username, password, email=None):
    db = client["mydatabase"]
    users = db["users"]
    user = {"username": username, "password": password, "email": email, "is_active": True, "is_staff": True}
    result = users.insert_one(user)
    return result.inserted_id

def get_user_by_username(client, username):
    db = client["mydatabase"]
    users = db["users"]
    user = users.find_one({"username": username})
    return user

def authenticate(client, request=None, username=None, password=None):
    user = get_user_by_username(client, username)
    if user and user["password"] == password and user["is_active"]:
        return user
    else:
        return None
def get_user(client, user_id):
    db = client["mydatabase"]
    users = db["users"]
    user = users.find_one({"_id": user_id})
    return user if user and user["is_active"] else None