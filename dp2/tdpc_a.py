N = int(input())
problems = list(map(int, input().split()))

max_score = sum(problems)
dp = [[False] * (max_score + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    score = problems[i - 1]
    for j in range(max_score + 1):
        dp[i][j] = dp[i - 1][j]

        if j == score:
            dp[i][j] = True
        if dp[i - 1][j - score]:
            dp[i][j] = True

print(sum(dp[N]))
