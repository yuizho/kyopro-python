# https://atcoder.jp/contests/abc081/tasks/abc081_b

import itertools


N = int(input())
A = list(map(int, input().split()))

result = 0
for i in itertools.count():
    if all([x % 2 == 0 for x in A]):
        A = list(map(lambda x: x // 2, A))
    else:
        result = i
        break

print(result)
