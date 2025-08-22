S = input()
N = len(S) + 1
A = [0] * N


for i in range(N - 1):
    if S[i] == "<":
        A[i + 1] += A[i] + 1

for i in range(N - 2, -1, -1):
    if S[i] == ">" and A[i] <= A[i + 1]:
        A[i] = A[i + 1] + 1

print(sum(A))
