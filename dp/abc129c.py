N, M = map(int, input().split())
brokens = set(int(input()) for _ in range(int(M)))

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    if i in brokens:
        continue

    from_1_steps_before = dp[i - 1]
    from_2_steps_before = 0
    if i >= 2:
        from_2_steps_before = dp[i - 2]

    dp[i] = (from_1_steps_before + from_2_steps_before) % 1000000007

print(dp[N])
