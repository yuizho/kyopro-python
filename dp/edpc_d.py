N, W = map(int, input().split())
# [(w, v)]
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = items[i - 1]

    for j in range(W + 1):
        # とりあえず一つ上のitemのdp行を引き継ぎ
        dp[i][j] = dp[i - 1][j]
        # 一つまえの行からナップサックに入るだけ価値を埋めていくイメージ
        # wが4ならでWが８ならj=4~8の間dp[i][j]に値が設定されていく
        # これにより、過去に取得した価値との足し合わせも実装される
        if j >= w:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

print(max(dp[N]))
