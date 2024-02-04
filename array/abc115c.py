# https://atcoder.jp/contests/abc115/tasks/abc115_c

N, K = map(int, input().split())
trees = []
for n in range(N):
    trees.append(int(input()))

trees.sort()
diffs = []
for n in range(N - K + 1):
    diffs.append(trees[n + K - 1] - trees[n])

print(min(diffs))
