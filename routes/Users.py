from flask_restful import Resource, request
from entities.User import User
from modules.Users.create_user.main import createUserController
from modules.Users.get_all_users.main import getAllUsersController
class Users(Resource):
    def get(self):
        result = getAllUsersController.handle()
        return result,200
    def post(self):
        result = createUserController.handle(request.get_json())
        return result,201
        