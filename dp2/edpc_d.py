N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]

        if j >= weight:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weight] + value)

print(dp[N][W])
