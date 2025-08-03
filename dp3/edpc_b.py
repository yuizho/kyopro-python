N, K = map(int, input().split())
steps = list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    min_cost = 10**18
    for j in range(1, K + 1):
        if j > i:
            break
        min_cost = min(min_cost, abs(steps[i - j] - steps[i]) + dp[i - j])
    dp[i] = min_cost

print(dp[N - 1])
