import collections
import math


N = int(input())
texts = [str(sorted(input())) for _ in range(N)]

counter = collections.Counter(texts)

result = 0
for count in counter.values():
    if count > 1:
        result += math.comb(count, 2)

print(result)
