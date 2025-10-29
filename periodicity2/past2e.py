N = int(input())
A = list(map(int, input().split()))

result = []
for i in range(N):
    x = i
    for j in range(1, N + 1):
        if A[x] - 1 == i:
            result.append(j)
            break
        else:
            x = A[x] - 1

print(" ".join(map(str, result)))
