from abc import abstractmethod, ABC


class IUsersRepo(ABC):
    @abstractmethod
    def get_user(self, id):
        return
    @abstractmethod
    def create_user(self, user):
        return
    @abstractmethod
    def get_users(self):
        return
    @abstractmethod
    def get_users_by_email(self, email):
        return
    @abstractmethod
    def get_users_by_name(self, name):
        return 