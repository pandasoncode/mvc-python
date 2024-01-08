from typing import List

from models.user import User

class UserService:
    def __init__(self):
        pass

    def get_all_users(self) -> 'List[User]':
        return [
            User("Juan", "juan@gmail.com"),
            User("Ana", "ana@gmail.com"),
            User("Pedro", "pedro@gmail.com"),
            User("Maria", "maria@gmail.com"),
        ]
