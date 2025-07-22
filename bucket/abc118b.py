from collections import Counter, defaultdict
import itertools


N, M = map(int, input().split())
Answers = [list(map(int, input().split()))[1:] for _ in range(N)]

result = 0
for v in Counter(itertools.chain(*Answers)).values():
    if v == N:
        result += 1

print(result)
