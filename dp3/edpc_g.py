from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

paths = [tuple(map(int, input().split())) for _ in range(M)]

graphs = defaultdict(list)
for f, t in paths:
    graphs[f].append(t)


dp: dict[int, int] = {}


def traverse(path: int) -> int:
    if not graphs[path]:
        return 0

    if path in dp:
        return dp[path]

    longest = 0
    for p in graphs[path]:
        longest = max(longest, traverse(p) + 1)

    dp[path] = longest
    return longest


longest = 0
for i in range(1, N + 1):
    longest = max(longest, traverse(i))

print(longest)
