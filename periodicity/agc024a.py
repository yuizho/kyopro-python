A, B, C, K = map(int, input().split())

if K % 2 == 0:
    # Kが偶数の場合
    print(A - B)
else:
    # Kが奇数の場合
    print(B - A)
