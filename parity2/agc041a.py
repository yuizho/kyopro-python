N, A, B = map(int, input().split())

diff = B - A

if diff % 2 == 0:
    print(diff // 2)
else:
    print(min((A - 1) + 1 + (B - A - 1) // 2, (N - B) + 1 + (B - A - 1) // 2))
