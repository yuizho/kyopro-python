import collections
import math


N = int(input())

d: collections.defaultdict[str, int] = collections.defaultdict(int)
for _ in range(N):
    d[str(sorted(input()))] += 1

result = 0
for v in d.values():
    result += math.comb(v, 2)

print(result)
