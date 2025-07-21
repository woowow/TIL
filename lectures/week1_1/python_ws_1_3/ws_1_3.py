users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.
def filtering_age(users):
    adult_list = []
    for user in users:
        if user['age'] > 18:
            adult_list.append(user)
    print(f"Adults: {adult_list}")
    return adult_list


def filtering_active(users):
    active_list = []
    for user in users:
        if user['is_active']:
            active_list.append(user)
    print(f"Active Users: {active_list}")
    return active_list


def filtering_combined(users):
    combined_list = []
    for user in users:
        if user['age'] > 18 and user['is_active']:
            combined_list.append(user)
    print(f"Active Adults: {combined_list}")

def main():

    filtering_age(users)
    filtering_active(users)
    filtering_combined(users)

if __name__ == "__main__":
    main()