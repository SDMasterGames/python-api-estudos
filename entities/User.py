class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __get__(self):
        return self.__dict__
