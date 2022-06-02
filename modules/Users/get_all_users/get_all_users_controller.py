class get_all_users_controller:
    def __init__(self, usecase) -> None:
        self.usecase = usecase
    def handle(self):
        return self.usecase.execute()