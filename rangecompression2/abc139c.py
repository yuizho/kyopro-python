N = int(input())
H = list(map(int, input().split()))

attempts = 0
result = 0
for i in range(1, N):
    if H[i - 1] >= H[i]:
        attempts += 1
    else:
        result = max(result, attempts)
        attempts = 0

result = max(result, attempts)
print(result)
