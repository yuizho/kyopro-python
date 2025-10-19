import collections

N = int(input())
A = list(map(int, input().split()))

# ステップ1: 累積和のリストSを作成する (S[0]=0 を忘れずに)
cum_sum = [0] * (N + 1)
for i in range(N):
    cum_sum[i + 1] = cum_sum[i] + A[i]

# ステップ2: 各数値が何回登場したかを数える
# S = [0, 1, -1, 0, 3] の場合
# counts は {0: 2, 1: 1, -1: 1, 3: 1} という辞書(のようなもの)になる
counts = collections.Counter(cum_sum)

ans = 0
# ステップ3: 各出現回数 k から、kC2 (ペアの数) を計算して足し合わせる
for k in counts.values():
    # kC2 = k * (k - 1) // 2
    ans += k * (k - 1) // 2

print(ans)
