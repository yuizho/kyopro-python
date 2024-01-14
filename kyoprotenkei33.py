import math


H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
    exit()

w_max = math.ceil(W / 2)
h_max = math.ceil(H / 2)

print(w_max * h_max)
