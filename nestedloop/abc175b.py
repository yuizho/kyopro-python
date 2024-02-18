N = int(input())
L = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[i] == L[j] or L[i] == L[k] or L[k] == L[j]:
                continue
            if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                result += 1

print(result)
