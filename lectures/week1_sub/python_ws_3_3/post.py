import user

class Post:
    def __init__(self, name, content):
        self.name = name
        self.content = content
    
    def display_post_info(self):
        print(f"Post(user={self.name}, content={self.content})")