S = input()
N = len(S)

dp = [False] * (N + 1)

# 空文字の場合はTrueというのを表現するために[0]はTrueにしているし、
# あとdpテーブルの長さはN + 1になってる
# 空の表現がdp[0]に入ってる分が + 1
dp[0] = True

words = ["dream", "dreamer", "erase", "eraser"]

for i in range(1, N + 1):
    for word in words:
        word_len = len(word)
        # 文字数がwordに足りない or wordの前の部分が作れない場合(評価不要)はスキップ
        if i < word_len or not dp[i - word_len]:
            continue

        # Sの現在のindex - wordの長さ ~ Sの現在のindexの文字がwordと一致してたらdp[i]はTrue(到達可能)をいれる
        if S[i - word_len : i] == word:
            dp[i] = True
            break

if dp[N]:
    print("YES")
else:
    print("NO")
