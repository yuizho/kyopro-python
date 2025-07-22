N = int(input())
hapinesses: list[list[int]] = [list(map(int, input().split())) for i in range(N)]

dp = [(0, 0, 0) for _ in range(N + 1)]

for day in range(1, N + 1):
    todays_hapinesses = hapinesses[day - 1]

    today_a = max(dp[day - 1][1], dp[day - 1][2]) + todays_hapinesses[0]
    today_b = max(dp[day - 1][0], dp[day - 1][2]) + todays_hapinesses[1]
    today_c = max(dp[day - 1][0], dp[day - 1][1]) + todays_hapinesses[2]

    dp[day] = (today_a, today_b, today_c)

print(max(dp[N]))
