N = int(input())
P = list(map(float, input().split()))

dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1.0

for i in range(1, N + 1):
    for j in range(i + 1):
        # i-1枚目まででj-1回表が出ていて、今回表
        prob1 = 0.0
        if j > 0:
            prob1 = dp[i - 1][j - 1] * P[i - 1]

        # i-1枚目まででj回表が出ていて、今回裏
        prob2 = dp[i - 1][j] * (1.0 - P[i - 1])
        # print(f"{i=}, {j=}, {prob1=}, {prob2=}")

        dp[i][j] = prob1 + prob2
        # print(dp)

result = 0.0
for j in range(N // 2 + 1, N + 1):
    result += dp[N][j]

print(result)
