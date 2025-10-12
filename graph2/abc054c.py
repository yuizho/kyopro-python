N, M = map(int, input().split())

graph: list[list[int]] = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(nexts: list[int], reached: list[bool]) -> int:
    if all(reached):
        return 1

    result = 0
    for n in nexts:
        if reached[n]:
            continue
        updated = list(reached)
        updated[n] = True
        result += dfs(graph[n], updated)

    return result


reached = [False] * N
reached[0] = True
print(
    dfs(
        graph[0],
        reached,
    )
)
