# 아래에 코드를 작성하시오.

class User:
    user_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_count += 1

    def __str__(self):
        return f"{self.name}\n{self.email}"

    def description():
        print("SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.")


u1 = User('Alice', 'alice@example.com')
u2 = User('Bob', 'bob@example.com')

print(u1)
print(u2)

print(f"현재까지 생성된 사용자 수: {User.user_count}")
User.description()