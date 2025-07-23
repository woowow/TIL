# 아래에 코드를 작성하시오.

class Post:
    post_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content
        Post.post_count += 1
    
    def __str__(self):
        return f"Title: {self.title}"

    def show_content(self):
        print(f"Content: {self.content}")
    
    @classmethod
    def total_posts(cls):
        print(f"Total posts: {cls.post_count}")
    
    @staticmethod
    def description():
        print("SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.")


p1 = Post('First Post', 'This is the content of the first post.')
print(p1)
p1.show_content()
p2 = Post('Second Post', 'This is the content of the second post.')
print(p2)
p2.show_content()
Post.total_posts()
Post.description()