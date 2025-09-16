A, B, K = map(int, input().split())

if K >= A + B:
    print(0, 0)
    exit()

if K > A:
    K -= A
    print(0, B - K)
else:
    print(A - K, B)
