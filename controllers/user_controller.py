# controller.py
from views.user_view import UserView
from services.user_service import UserService
from models.user import User

class UserController:
    def __init__(self):
        self.user_view = UserView()
        self.user_service = UserService()

    def list_users(self):
        users: list[User] = self.user_service.get_all_users()
        self.user_view.show_user_list(users)
