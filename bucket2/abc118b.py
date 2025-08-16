import collections
import itertools


N, M = map(int, input().split())
preferences: list[list[int]] = []
for _ in range(N):
    preferences.append(list(map(int, input().split()))[1:])

d: collections.defaultdict[int, int] = collections.defaultdict(int)
for p in itertools.chain.from_iterable(preferences):
    d[p] += 1

result = 0
for k, v in d.items():
    if v == N:
        result += 1

print(result)
