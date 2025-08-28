import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

countries: list[list[int]] = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    countries[a].append(b)


def dfs(current, visited):
    if current in visited:
        return
    visited.add(current)

    for next in countries[current]:
        dfs(next, visited)


result = 0
for i in range(N):
    visited: set[int] = set()
    dfs(i, visited)
    result += len(visited)

print(result)
