N = int(input())

users: set[str] = set()
for i in range(1, N + 1):
    user = input()
    if user not in users:
        users.add(user)
        print(i)
