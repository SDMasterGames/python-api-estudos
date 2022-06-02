from repositories.implements.user_repo_memory import UserRepoMemory
from .create_user_usecase import create_user_usecase
from  .create_user_controller import create_user_controller

UserRepository = UserRepoMemory()

createUserUseCase = create_user_usecase(UserRepository)

createUserController = create_user_controller(createUserUseCase)
if __name__ == '__main__':
    createUserController
    createUserUseCase