N, L = map(int, input().split())
hurdles = set(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

dp = [float("inf")] * (L + 1)
dp[0] = 0

cost1 = T1
cost2 = T1 + T2
cost3 = T1 + 3 * T2

for i in range(1, L + 1):
    hardle_cost = 0 if i > L else (T3 if i in hurdles else 0)

    dp[i] = min(dp[i], cost1 + dp[i - 1] + hardle_cost)

    if i - 2 >= 0:
        dp[i] = min(dp[i], cost2 + dp[i - 2] + hardle_cost)

    if i - 4 >= 0:
        dp[i] = min(dp[i], cost3 + dp[i - 4] + hardle_cost)

result = dp[L]

# 候補2: L-1 から 2mジャンプで1m進む
result = min(result, dp[L - 1] + T1 // 2 + T2 // 2)

# 候補3: L-2 から 4mジャンプで2m進む
result = min(result, dp[L - 2] + T1 // 2 + 3 * T2 // 2)

# 候補4: L-3 から 4mジャンプで3m進む
result = min(result, dp[L - 3] + T1 // 2 + 5 * T2 // 2)

print(result)
