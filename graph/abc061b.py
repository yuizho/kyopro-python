N, M = map(int, input().split())
A = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    A[a - 1] += 1
    A[b - 1] += 1

for a in A:
    print(a)
