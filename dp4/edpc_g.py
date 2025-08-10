import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
nodes = [tuple(map(int, input().split())) for _ in range(M)]

graphs: list[list[int]] = [[] for _ in range(N + 1)]
for i in range(M):
    node = nodes[i]
    f = node[0]
    t = node[1]
    graphs[f].append(t)

# print(graphs)

dp = [-1 for _ in range(N + 1)]


def traverse(edge: int) -> int:
    if not graphs[edge]:
        return 0

    if dp[edge] != -1:
        return dp[edge]

    max_dist = 0
    for e in graphs[edge]:
        max_dist = max(max_dist, traverse(e) + 1)
    dp[edge] = max_dist
    return max_dist


for i in range(1, N + 1):
    traverse(i)

print(max(dp))
