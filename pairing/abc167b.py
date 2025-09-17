A, B, C, K = map(int, input().split())

result = 0

result += min(K, A)
K -= min(K, A)
if K <= 0:
    print(result)
    exit()

K -= min(K, B)
if K <= 0:
    print(result)
    exit()

result -= min(K, C)

print(result)
