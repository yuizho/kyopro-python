N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

max_value = sum(map(lambda x: x[1], items))

INF = 10**20
dp = [[INF] * (max_value + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = items[i - 1]
    for j in range(max_value + 1):
        dp[i][j] = dp[i - 1][j]

        if j >= v:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)


result = 0
for v, w in enumerate(dp[N]):
    if w <= W:
        result = max(result, v)

print(result)
