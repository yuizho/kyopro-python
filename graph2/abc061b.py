import collections


N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    print(len(graph[i]))
