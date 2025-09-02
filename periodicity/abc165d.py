import math

A, B, N = map(int, input().split())

x = N
if x >= B:
    x = B - 1

result = math.floor(A * x / B) - A * math.floor(x / B)
print(result)
