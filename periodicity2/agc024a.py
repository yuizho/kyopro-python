A, B, C, K = map(int, input().split())

if K % 2 == 0:
    # Kが偶数
    print(A - B)
else:
    # Kが奇数
    print(B - A)
