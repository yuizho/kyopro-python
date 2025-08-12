A, B, W = map(int, input().split())

# みかんはAグラム以上Bグラム以下。
# この中からいくつかみかんを選んでWキログラムになる (みかんの重さは整数とは限らない)
# 個数の最小値と最大値を求める

W_g = W * 1000

# 最小個数を非常に大きな数、最大個数を-1で初期化
min_count = 10**9
max_count = -1

# 個数nを1からありえる最大値まで試す
# W_gを最軽量Aで割った数より多くなることはないので、W_gまでで十分
for n in range(1, W_g + 1):
    # n個の場合の最小重量と最大重量を計算
    min_weight = n * A
    max_weight = n * B

    # 目的の重量W_gが、n個で作れる重量の範囲内かチェック
    if min_weight <= W_g and W_g <= max_weight:
        # 範囲内なら、最小個数と最大個数を更新
        min_count = min(min_count, n)
        max_count = max(max_count, n)

# ループ後にmax_countが更新されていなければ、解はなかったということ
if max_count == -1:
    print("UNSATISFIABLE")
else:
    print(min_count, max_count)
