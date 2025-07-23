N = int(input())
steps = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(steps[0] - steps[1])

for i in range(2, N):
    one_step = abs(steps[i - 1] - steps[i]) + dp[i - 1]
    two_step = abs(steps[i - 2] - steps[i]) + dp[i - 2]

    dp[i] = min(one_step, two_step)

print(dp[N - 1])
