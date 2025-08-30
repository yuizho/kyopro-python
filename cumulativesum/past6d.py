N, K = map(int, input().split())
A = list(map(int, input().split()))

cum_sum = [0] * (N + 1)
for i in range(1, N + 1):
    cum_sum[i] = cum_sum[i - 1] + A[i - 1]

# print(cum_sum)

left = 0
right = K
while right <= N:
    print(cum_sum[right] - cum_sum[left])
    left += 1
    right += 1
