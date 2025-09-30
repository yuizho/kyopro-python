import collections


N, M = map(int, input().split())

dd: collections.defaultdict[int, int] = collections.defaultdict(int)

for _ in range(N):
    ans = list(map(int, input().split()))
    for a in ans[1:]:
        dd[a] += 1

result = 0
for count in dd.values():
    if count == N:
        result += 1

print(result)
