N, K = map(int, input().split())
steps = list(map(int, input().split()))

INF = 10**18

dp = [INF] * N
dp[0] = 0

for i in range(N):
    for k in range(1, K + 1):
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + abs(steps[i] - steps[i - k]))

print(dp[N - 1])
