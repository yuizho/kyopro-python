N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

total_value = sum(map(lambda x: x[1], items))

dp = [[10**18] * (total_value + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = items[i - 1]
    for j in range(total_value + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= v:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)
    # print(dp)

result = 0
for i, w in enumerate(dp[N]):
    if w <= W:
        result = max(result, i)

print(result)
