s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            # 文字が一致する場合はdpのカウント更新
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 一致しない場合はdpテーブルの上 or 左のカウント数の大きい方を引き継ぎ
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[i])

lcs = ""
i, j = len_s, len_t

while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        lcs = s[i - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(lcs)
