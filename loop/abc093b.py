# https://atcoder.jp/contests/abc093/tasks/abc093_b

A, B, K = map(int, input().split())

result = set([])
for i, v in enumerate(range(A, B + 1)):
    if i >= K:
        break
    result.add(v)

for i, v in enumerate(range(B, A - 1, -1)):
    if i >= K:
        break
    result.add(v)

for v in sorted(list(result)):
    print(v)
