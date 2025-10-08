import collections


N, M, Q = map(int, input().split())
graph: dict[int, list[int]] = collections.defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

colors = list(map(int, input().split()))

for _ in range(Q):
    qt, x, *y = map(int, input().split())
    x -= 1
    print(colors[x])
    if qt == 1:
        neibors = graph[x]
        for n in neibors:
            colors[n] = colors[x]
    else:
        colors[x] = y[0]
