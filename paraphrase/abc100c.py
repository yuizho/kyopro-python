N = int(input())
A = list(map(int, input().split()))

result = 0
for i in range(N):
    if A[i] % 2 == 0:
        while A[i] % 2 == 0:
            result += 1
            A[i] = A[i] // 2

print(result)
