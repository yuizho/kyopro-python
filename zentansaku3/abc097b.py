X = int(input())

result = 1
for b in range(1, X + 1):
    for p in range(2, X + 1):
        attempt = b**p
        # print(b, j, attempt)
        if attempt > X:
            break
        result = max(result, attempt)

print(result)
