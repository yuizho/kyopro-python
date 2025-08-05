from collections import defaultdict
from typing import DefaultDict

N, M = map(int, input().split())

paths = [tuple(map(int, input().split())) for _ in range(M)]

graphs = defaultdict(list)
for f, t in paths:
    graphs[f].append(t)


dp: DefaultDict[int, int] = defaultdict(int)


def traverse(path) -> int:
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
for k in list(graphs.keys()):
    longest = max(longest, traverse(k))

print(longest)
