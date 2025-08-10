N = int(input())
probs = list(map(float, input().split()))

dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(i + 1):
        dp[i][j] += dp[i - 1][j] * (1 - probs[i - 1])
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * probs[i - 1]
    # print(dp[i])

result = 0.0
for i in range(N // 2 + 1, N + 1):
    result += dp[N][i]

print(result)
