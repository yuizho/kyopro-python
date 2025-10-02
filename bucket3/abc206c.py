from collections import Counter
import math


N = int(input())
counter = Counter(map(int, input().split()))

all_comb = math.comb(sum(counter.values()), 2)
needs_removing_comb = 0
for count in counter.values():
    needs_removing_comb += math.comb(count, 2)


print(all_comb - needs_removing_comb)
