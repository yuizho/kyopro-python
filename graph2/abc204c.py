import sys
from typing import List

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

roads: List[List[int]] = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append(b)


pairs: set[tuple[int, int]] = set()


def dfs(start: int, current: int, visited: set[int]):
    if current in visited:
        return
    pairs.add((start, current))

    visited.add(current)
    if len(visited) == N:
        return

    for next in roads[current]:
        if (start, next) in pairs:
            continue
        dfs(start, next, visited)


for i in range(N):
    visited: set[int] = set()
    dfs(i, i, visited)

print(len(pairs))
