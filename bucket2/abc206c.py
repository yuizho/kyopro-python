from collections import Counter
import math


N = int(input())
numbers = Counter(map(int, input().split()))
duplicated_count = 0
for count in numbers.values():
    if count > 1:
        duplicated_count += math.comb(count, 2)

print(math.comb(N, 2) - duplicated_count)
