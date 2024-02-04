# https://atcoder.jp/contests/typical90/tasks/typical90_bx

import bisect
import itertools

N = int(input())
pieces = list(map(int, input().split()))

total = sum(pieces)
if total % 10 != 0:
    print("No")
    exit()

pieces *= 2

accum = [0] + list(itertools.accumulate(pieces))

target = total // 10

for left in range(N):
    right = bisect.bisect_left(accum, target + accum[left])
    if accum[right] - accum[left] == target:
        print("Yes")
        exit()

print("No")
