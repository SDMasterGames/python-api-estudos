class create_user_usecase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user):
        return self.user_repo.create_user(user)