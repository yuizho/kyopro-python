N, K = map(int, input().split())
P = list(map(int, input().split()))

cum_expected = [0.0] * (N + 1)
for i in range(1, N + 1):
    current_expected_value = (P[i - 1] + 1) / 2
    cum_expected[i] = cum_expected[i - 1] + current_expected_value

# print(cum_expected)

left = 0
right = K
result = 0.0
while right <= N:
    result = max(result, cum_expected[right] - cum_expected[left])
    left += 1
    right += 1

print(result)
