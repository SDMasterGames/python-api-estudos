from repositories.implements.user_repo_memory import UserRepoMemory
from .get_all_users_usecase import get_all_users_usecase
from .get_all_users_controller import get_all_users_controller

UserRepository = UserRepoMemory()

getAllUsersUseCase = get_all_users_usecase(UserRepository)

getAllUsersController = get_all_users_controller(getAllUsersUseCase)