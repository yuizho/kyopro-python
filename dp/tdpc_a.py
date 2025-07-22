N = int(input())
points = list(map(int, input().split()))
all_points = sum(points)

dp = [[False] * (all_points + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    point = points[i - 1]
    for j in range(all_points + 1):
        dp[i][j] = dp[i - 1][j]
        if j == point:
            dp[i][j] = True
        if dp[i - 1][j - point]:
            dp[i][j] = True

        # print(f"{point=}, {i=}, {j=}, {dp[i]=}")

print(sum(dp[N]))
