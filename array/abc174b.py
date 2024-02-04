N, D = map(int, input().split())
distances = []
for n in range(N):
    x, y = map(int, input().split())
    distances.append(x * x + y * y)

result = len(list(filter(lambda x: D * D >= x, distances)))
print(result)
