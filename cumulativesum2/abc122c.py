N, Q = map(int, input().split())
S = input()
cum = [0] * N
for i in range(1, N):
    if S[i - 1] == "A" and S[i] == "C":
        cum[i] = cum[i - 1] + 1
    else:
        cum[i] = cum[i - 1]

for _ in range(Q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    print(cum[right] - cum[left])
