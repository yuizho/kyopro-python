N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

max_value = 1000 * N
INF = 10**9 + 1
dp = [[INF] * (max_value + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for j in range(max_value + 1):
        unuse = dp[i - 1][j]
        use = INF
        if j >= value:
            if dp[i - 1][j - value] != INF:
                use = dp[i - 1][j - value] + weight
        dp[i][j] = min(use, unuse)
    print(f"{i=}, {dp[i]}")

result = 0
for v in range(max_value, -1, -1):
    if dp[N][v] <= W:
        result = v
        break

print(result)
