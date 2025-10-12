N, M = map(int, input().split())

graph: list[set[int]] = [set() for _ in range(N)]
edges: list[tuple[int, int]] = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].add(b)
    graph[b].add(a)
    edges.append((a, b))


def dfs(attempted_graph: list[set[int]], current: int, visited: set[int]):
    if current in visited:
        return
    if len(attempted_graph[current]) == 0:
        return
    if len(visited) == N:
        return

    visited.add(current)

    for next in attempted_graph[current]:
        dfs(attempted_graph, next, visited)


result = 0
for removed_a, removed_b in edges:
    copied_graph = []
    for i in range(N):
        copied_graph.append(graph[i].copy())
    copied_graph[removed_a].remove(removed_b)
    copied_graph[removed_b].remove(removed_a)
    visited: set[int] = set()
    dfs(copied_graph, 0, visited)
    if len(visited) < N:
        result += 1

print(result)
