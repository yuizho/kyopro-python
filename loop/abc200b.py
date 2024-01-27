# https://atcoder.jp/contests/abc200/tasks/abc200_b

N, K = map(int, input().split())

for k in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = int(str(N) + "200")

print(N)
