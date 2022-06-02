class get_all_users_usecase:
    def __init__(self,user_repo) -> None:
        self.user_repo = user_repo
    def execute(self):
        return self.user_repo.get_users()