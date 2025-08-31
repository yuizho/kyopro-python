import collections

N = int(input())
A = list(map(int, input().split()))

# 1. 累積和のリストを作成する (先頭に0を追加するのがポイント)
cum_sum = [0] * (N + 1)
for i in range(N):
    cum_sum[i + 1] = cum_sum[i] + A[i]

# 2. 累積和に各数値が何回登場したかを数える
# collections.Counter を使うと便利
counts = collections.Counter(cum_sum)

# print(cum_sum)
# print(counts)

ans = 0
# 3. 各数値の出現回数 k から、組み合わせの数 kC2 を計算して足し合わせる
for k in counts.values():
    ans += k * (k - 1) // 2

print(ans)
