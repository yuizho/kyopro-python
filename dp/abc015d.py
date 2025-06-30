W = int(input())
N, K = map(int, input().split())
screen_shots = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(K + 1)]

for width, priority in screen_shots:
    for k in range(K, 0, -1):
        for j in range(W, width - 1, -1):
            # 1枚目
            if k - 1 == 0 and j - width == 0:
                dp[k][j] = max(dp[k][j], priority)
            # 2枚目移行
            elif dp[k - 1][j - width] > 0:
                dp[k][j] = max(dp[k][j], dp[k - 1][j - width] + priority)

result = 0
for row in dp:
    result = max(result, max(row))

print(result)
