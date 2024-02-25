X = int(input())

result = 1
for b in range(1, X):
    for p in range(2, X):
        if b**p > X:
            break
        else:
            result = max(result, b**p)

print(result)
