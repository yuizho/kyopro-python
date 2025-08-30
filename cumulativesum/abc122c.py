N, Q = map(int, input().split())
S = input()

comulative_sums = [0] * (N + 1)
for i in range(2, N + 1):
    comulative_sums[i] = comulative_sums[i - 1]
    if S[i - 2] + S[i - 1] == "AC":
        comulative_sums[i] += 1

# print(comulative_sums)

for _ in range(Q):
    left, right = map(int, input().split())
    print(comulative_sums[right] - comulative_sums[left])
