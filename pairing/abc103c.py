import math


N = int(input())
A = list(map(int, input().split()))

lcm = math.lcm(*A)
print(sum(map(lambda x: (lcm - 1) % x, A)))
