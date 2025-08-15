N, K = map(int, input().split())

# count1: 1からNまでのKの倍数の個数
count1 = N // K
ans = count1**3

# Kが偶数の場合、もう1つのパターンを考慮する
if K % 2 == 0:
    # K/2だけ余る数の最初の値
    half_k = K // 2

    # 1からNまでに「Kで割るとK/2余る数」がいくつあるか
    # half_k, half_k + K, half_k + 2K, ...
    # Nがhalf_kより小さい場合は0個
    if N >= half_k:
        # Nにhalf_kを足してからKで割ると個数が求まる
        count2 = (N + half_k) // K
        ans += count2**3

print(ans)
