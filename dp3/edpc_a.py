N = int(input())
steps = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(steps[1] - steps[0])

for i in range(2, N):
    one_step_cost = abs(steps[i - 1] - steps[i]) + dp[i - 1]
    two_step_cost = abs(steps[i - 2] - steps[i]) + dp[i - 2]
    dp[i] = min(one_step_cost, two_step_cost)

print(dp[N - 1])
