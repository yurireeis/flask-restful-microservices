from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password_is_valid(password):
        return user

def identity(payload):
    return UserModel.find_by_username(payload['identity'])
