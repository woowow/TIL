import sns

s1 = sns.SNS()

s1.add_post("john_doe", "Hello, this is my first post!")
s1.add_post("jane_doe", "Hi everyone, glad to be here!")

s1.get_posts()