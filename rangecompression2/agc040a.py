S = input()
A = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == "<":
        A[i + 1] = A[i] + 1

# print(A)

for i in range(len(S) - 1, -1, -1):
    if S[i] == ">" and A[i] <= A[i + 1]:
        A[i] = A[i + 1] + 1

# print(A)
print(sum(A))
