N = int(input())
S = input()

# 1. 全てのペアの総数を計算
total_substrings = N * (N + 1) // 2

# 2. 条件を満たさないペア（同じ文字だけの部分文字列）を引いていく
bad_substrings = 0
count = 1
for i in range(N - 1):
    if S[i] == S[i + 1]:
        # 前の文字と同じなら、連続カウントを増やす
        count += 1
    else:
        # 文字が変わったら、そこまでの連続ブロックから作られるペア数を加算
        bad_substrings += count * (count + 1) // 2
        # 連続カウントをリセット
        count = 1

# 最後の連続ブロックの分を加算する
bad_substrings += count * (count + 1) // 2

# 3. 全体から引く
ans = total_substrings - bad_substrings
print(ans)
