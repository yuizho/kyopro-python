K, S = map(int, input().split())

result = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - (x + y)
        if 0 <= z <= K:
            result += 1

print(result)
