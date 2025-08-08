N = int(input())
steps = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(steps[0] - steps[1])

for i in range(2, N):
    dp[i] = min(
        abs(steps[i - 1] - steps[i]) + dp[i - 1],
        abs(steps[i - 2] - steps[i]) + dp[i - 2],
    )

print(dp[N - 1])
