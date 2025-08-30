N = int(input())
A = list(map(int, input().split()))

cum_sum = [0] * (N + 1)
for i in range(1, N + 1):
    cum_sum[i] = cum_sum[i - 1] + A[i - 1]

for i in range(1, N + 1):
    left = 0
    right = left + i
    m = 0
    while right <= N:
        m = max(cum_sum[right] - cum_sum[left], m)
        left += 1
        right += 1
    print(m)
