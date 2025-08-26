N, M, Q = map(int, input().split())
graph: list[list] = [[0, []] for _ in range(N)]

for _ in range(M):
    f, t = map(int, input().split())
    graph[f - 1][1].append(t)
    graph[t - 1][1].append(f)

colors = list(map(int, input().split()))
for i in range(N):
    graph[i][0] = colors[i]

for i in range(Q):
    query = input()
    if query.startswith("1"):
        _, x = map(int, query.split())
        current_color = graph[x - 1][0]
        print(current_color)
        next_edges = graph[x - 1][1]
        for edge in next_edges:
            graph[edge - 1][0] = current_color
    else:
        _, x, y = map(int, query.split())
        current_color = graph[x - 1][0]
        print(current_color)
        graph[x - 1][0] = y
