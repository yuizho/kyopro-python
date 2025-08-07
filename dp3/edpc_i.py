N = int(input())
probs = list(map(float, input().split()))

# コインを投げた回数を表が出た回数で2次元dpを作る
dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1.0

for i in range(1, N + 1):
    for j in range(0, i + 1):
        prob1 = 0.0
        if j > 0:
            prob1 = dp[i - 1][j - 1] * probs[i - 1]

        prob2 = dp[i - 1][j] * (1.0 - probs[i - 1])

        dp[i][j] = prob1 + prob2

result = 0.0
for j in range(N // 2 + 1, N + 1):
    result += dp[N][j]

print(result)
