import math

A, B, W = map(int, input().split())
W *= 1000

min_n = math.ceil(W / B)
max_n = W // A

if min_n > max_n:
    print("UNSATISFIABLE")
else:
    print(min_n, max_n)
