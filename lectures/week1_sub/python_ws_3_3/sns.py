import user
import post

class SNS:
    
    users = []
    posts = []

    def __init__(self):
        pass

    def add_user(cls, username, email):
        
        u1 = user.User(username, email)
        cls.users.append(u1)

        return u1
    
    def add_post(cls, user, content):
        
        p1 = post.Post(user, content)
        cls.posts.append(p1)

        return p1

    def get_posts(cls):
        for post in cls.posts:
            post.display_post_info()

        return cls.posts