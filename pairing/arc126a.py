T = int(input())

for _ in range(T):
    N2, N3, N4 = map(int, input().split())
    ans = 0

    # ステップ1: 3の棒のペアを処理する
    # ① 4+3+3 を作る
    k = min(N4, N3 // 2)
    ans += k
    N4 -= k
    N3 -= k * 2

    # ② 3+3+2+2 を作る
    k = min(N3 // 2, N2 // 2)
    ans += k
    N3 -= k * 2
    N2 -= k * 2

    # ステップ2: 4の棒を処理する
    # ③ 4+4+2 を作る
    k = min(N4 // 2, N2)
    ans += k
    N4 -= k * 2
    N2 -= k

    # ④ 4+2+2+2 を作る
    k = min(N4, N2 // 3)
    ans += k
    N4 -= k
    N2 -= k * 3

    # ステップ3: 2の棒を処理する
    # ⑤ 2+2+2+2+2 を作る
    k = N2 // 5
    ans += k

    print(ans)
