import math


N, D = map(int, input().split())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

result = 0
for r1 in range(N):
    for r2 in range(r1 + 1, N):
        s = sum([(points[r1][c] - points[r2][c]) ** 2 for c in range(D)])
        sqrted = math.sqrt(s)
        if str(sqrted).endswith(".0"):
            result += 1

print(result)
