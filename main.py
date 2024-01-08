# main.py
from controllers.user_controller import UserController

if __name__ == "__main__":
    user_controller = UserController()
    user_controller.list_users()
