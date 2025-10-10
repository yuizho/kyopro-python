N, M = map(int, input().split())

counts: list[int] = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        counts[a] += 1
    if a < b:
        counts[b] += 1

result = 0
for c in counts:
    if c == 1:
        result += 1

print(result)
