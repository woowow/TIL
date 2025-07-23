# 아래에 코드를 작성하시오.

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

class AdminUser(User):
    permissions = ""

    def __init__(self, name, email, authority):
        super().__init__(name, email)
        self.permissions = authority
    
    def show_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Permissions: {self.permissions}")


u1 = User('Alice', 'alice@example.com')
u2 = User('Bob', 'bob@example.com')
au1 = AdminUser('Charlie', 'charlie@example.com', 'Full Access')

u1.show_info()
u2.show_info()
au1.show_info()