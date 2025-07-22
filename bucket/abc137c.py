from collections import defaultdict
from math import factorial


N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]

d: dict[str, int] = defaultdict(int)
for s in S:
    d[s] += 1

result = 0
for k in d:
    if d[k] > 1:
        n = d[k]
        result += n * (n - 1) // 2

print(result)
