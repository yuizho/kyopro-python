N = int(input())
A = list(map(int, input().split()))

result = 0
i = 0
while i < N:
    j = i
    while j < N and A[j] == A[i]:
        j += 1

    result += (j - i) // 2

    i = j

print(result)
