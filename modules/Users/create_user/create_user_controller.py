class create_user_controller:
    def __init__(self, useCase):
        self.useCase = useCase

    def handle(self,body):
        return self.useCase.execute(body)