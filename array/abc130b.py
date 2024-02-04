# https://atcoder.jp/contests/abc130/tasks/abc130_b

N, X = map(int, input().split())
points = list(map(int, input().split()))

D = 0
result = 1
for p in points:
    D += p
    if X < D:
        break
    result += 1

print(result)
