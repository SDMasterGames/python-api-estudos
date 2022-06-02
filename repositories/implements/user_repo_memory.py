from repositories.abstract_user_repo import IUsersRepo
users = []
class UserRepoMemory(IUsersRepo):
    def get_user(self, id):
        for user in users:
            if user.id == id:
                return user
        return None

    def create_user(self, user):
        users.append(user)
        return user

    def get_users(self):
        return users

    def get_users_by_email(self, email):
        return

    def get_users_by_name(self, name):
        return