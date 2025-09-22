K, A, B = map(int, input().split())

# 戦略1：ひたすら叩く場合の枚数
ans1 = 1 + K

# 戦略2：円との交換を狙う
# まず、交換で得するかの判定 (B-A > 2)
# B-A <= 2 なら交換する意味がないので、ans1が答え
if B - A <= 2:
    print(ans1)
else:
    # 投資（ビスケットをA枚にする）に必要な操作回数
    ops_to_start = A - 1

    # 投資期間中に操作回数が尽きてしまう場合
    if K <= ops_to_start:
        print(ans1)
    else:
        # 投資後の状態
        # ビスケット: A枚
        # 残り操作回数: K - ops_to_start
        rem_ops = K - ops_to_start

        # 交換サイクルで増える枚数
        profit = (rem_ops // 2) * (B - A)

        # サイクル後の余った操作で増える枚数
        rem_cookies = rem_ops % 2

        # 最終的な枚数
        ans2 = A + profit + rem_cookies
        print(ans2)
