N = int(input())

cum_1 = [0] * (N + 1)
cum_2 = [0] * (N + 1)
for i in range(1, N + 1):
    c, p = map(int, input().split())
    cum_1[i] = cum_1[i - 1]
    cum_2[i] = cum_2[i - 1]
    if c == 1:
        cum_1[i] += p
    else:
        cum_2[i] += p

# print(cum_1)
# rint(cum_2)

Q = int(input())
for _ in range(Q):
    left, right = map(int, input().split())
    print(cum_1[right] - cum_1[left - 1], cum_2[right] - cum_2[left - 1])
