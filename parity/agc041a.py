N, A, B = map(int, input().split())

dist = B - A
if dist % 2 == 0:
    print(dist // 2)
else:
    dist_of_edge = min(A - 1, N - B)
    # +1は端から中央によっていくときに奇数になるように調整ターンが必要なのでその分
    print(dist // 2 + 1 + dist_of_edge)
