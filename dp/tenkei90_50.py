N, L = map(int, input().split())

MOD = (10**9) + 7

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(1, N + 1):
    one_step = dp[i - 1]
    n_step = 0
    if i >= L:
        n_step = dp[i - L]

    dp[i] = (one_step + n_step) % MOD

print(dp[N])
