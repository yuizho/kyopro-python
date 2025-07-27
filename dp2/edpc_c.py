N = int(input())
days = []
for _ in range(N):
    days.append(list(map(int, input().split())))

dp = [[0] * (3) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + days[i - 1][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + days[i - 1][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + days[i - 1][2]

print(max(dp[N]))
