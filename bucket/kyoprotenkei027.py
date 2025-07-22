from collections import defaultdict


N = int(input())
users = [input() for _ in range(N)]

d = defaultdict(list)
for i, u in enumerate(users):
    d[u].append(i + 1)

for v in d.values():
    print(v[0])
