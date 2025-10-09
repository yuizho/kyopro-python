N, M = map(int, input().split())
H = list(map(int, input().split()))

good_routes: list[list[bool]] = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] > H[b]:
        good_routes[a].append(True)
        good_routes[b].append(False)
    elif H[a] < H[b]:
        good_routes[a].append(False)
        good_routes[b].append(True)
    else:
        good_routes[a].append(False)
        good_routes[b].append(False)

result = 0
for i in range(N):
    if all(good_routes[i]):
        result += 1

print(result)
