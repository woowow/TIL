import user

def main():
    u1 = user.User('Alice', 'alice@example.com')
    u2 = user.User('Bob', 'bob@example.com')

    u1.display_info()
    u2.display_info()

if __name__=="__main__":
    main()