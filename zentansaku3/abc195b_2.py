import math


A, B, W = map(int, input().split())

W_G = W * 1000

max_count = W_G // A
min_count = math.ceil(W_G / B)

if max_count < min_count:
    print("UNSATISFIABLE")
else:
    print(min_count, max_count)
