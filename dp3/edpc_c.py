N = int(input())
activities = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    a = max(dp[i - 1][1], dp[i - 1][2]) + activities[i - 1][0]
    b = max(dp[i - 1][0], dp[i - 1][2]) + activities[i - 1][1]
    c = max(dp[i - 1][0], dp[i - 1][1]) + activities[i - 1][2]
    dp[i] = [a, b, c]

print(max(dp[N]))
