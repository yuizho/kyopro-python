# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# remainders[i] には、Aの要素を200で割った余りが i になるものの個数を格納する
# 長さ200のリストを0で初期化
remainders = [0] * 200

# 手順1: 各数値の余りを計算し、カウントする
for x in A:
    remainders[x % 200] += 1

# 答えを格納する変数
ans = 0

# 手順2: 各余りのグループについて、ペアの数を計算して足し合わせる
for count in remainders:
    # count個の中から2つを選ぶ組み合わせの数を計算
    # c C 2 = c * (c - 1) / 2
    if count >= 2:
        ans += count * (count - 1) // 2

# 答えを出力
print(ans)
