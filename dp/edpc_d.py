N, W = map(int, input().split())
# [(w, v)]
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)

for n in range(N):
    w, v = items[n]
    for i in range(W, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
