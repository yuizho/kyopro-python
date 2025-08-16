N = int(input())
users = [input() for _ in range(N)]

applicated = {}
for i, user in enumerate(users):
    if user in applicated:
        continue
    applicated[user] = i + 1

for i in applicated.values():
    print(i)
