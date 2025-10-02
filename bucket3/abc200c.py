from collections import Counter
import math


N = int(input())
A = list(map(int, input().split()))

mods = Counter(map(lambda x: x % 200, A))

result = 0
for count in mods.values():
    result += math.comb(count, 2)

print(result)
