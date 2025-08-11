K, S = map(int, input().split())

# 0 <= X, Y, Z <= K
# X + Y + Z = S が何通りあるか？

result = 0
for x in range(0, K + 1):
    for y in range(0, K + 1):
        z = S - x - y
        if 0 <= z <= K:
            # print(x, y, z)
            result += 1

print(result)
