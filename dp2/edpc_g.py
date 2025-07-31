N, M = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(M)]

if N == 2:
    print(1)
    exit(0)

dp = [[0] * N for _ in range(M + 1)]

for i in range(1, M + 1):
    f, t = graph[i - 1]
    dp[i] = dp[i - 1]
    dp[i][t - 1] = max(dp[i - 1][t - 1], dp[i - 1][f - 1] + 1)

print(max(dp[M]))
