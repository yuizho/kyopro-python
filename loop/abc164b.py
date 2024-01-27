# https://atcoder.jp/contests/abc164/tasks/abc164_b

import itertools


A, B, C, D = map(int, input().split())

for i in itertools.count():
    if i % 2 == 0:
        C -= B
    else:
        A -= D

    if A <= 0 or C <= 0:
        break

print("Yes" if A > 0 else "No")
