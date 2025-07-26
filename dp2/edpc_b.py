N, K = map(int, input().split())
steps = list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    minimum = 10**16
    for j in range(1, K + 1):
        if i >= j:
            minimum = min(minimum, abs(steps[i - j] - steps[i]) + dp[i - j])
    dp[i] = minimum

print(dp[N - 1])
