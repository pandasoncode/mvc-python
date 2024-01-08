# view.py
from models.user import User

class UserView:
    def show_user(self, user: User) -> None:
        print(f"Nombre: {user.name}")
        print(f"Correo: {user.mail}")

    def create_user(self) -> User:
        name = input("Ingrese el nombre del usuario: ")
        mail = input("Ingrese el correo del usuario: ")
        return User(name, mail)
    
    def show_user_list(self, users: 'list[User]') -> None:
        for u in users:
            self.show_user(u)
            print("---------------")
