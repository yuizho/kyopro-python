N, K = map(int, input().split())

A = list(map(int, input().split()))
cum = [0] * (N + 1)
for i in range(1, N + 1):
    cum[i] = cum[i - 1] + A[i - 1]

for i in range(K, N + 1):
    print(cum[i] - cum[i - K])
