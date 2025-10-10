N, M = map(int, input().split())

routes: list[list[int]] = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    routes[a].append(b)

first_routes = routes[0]
result = "IMPOSSIBLE"
for fr in first_routes:
    if N - 1 in routes[fr]:
        result = "POSSIBLE"

print(result)
