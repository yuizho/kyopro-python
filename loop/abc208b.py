# https://atcoder.jp/contests/abc208/tasks/abc208_b

import math


P = int(input())


# Pより小さく一番大きい硬貨でできるだけ払うを繰り返す
result = 0
for i in range(10, 0, -1):
    f = math.factorial(i)
    for n in range(100):
        if P >= f:
            P -= f
            result += 1
    if P == 0:
        break

print(result)
