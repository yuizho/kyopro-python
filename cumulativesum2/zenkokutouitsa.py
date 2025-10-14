N = int(input())
A = list(map(int, input().split()))

cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + A[i]

for k in range(1, N + 1):
    max_sum = 0
    for i in range(k, N + 1):
        # print(i - k, i, cum)
        max_sum = max(max_sum, cum[i] - cum[i - k])

    print(max_sum)
