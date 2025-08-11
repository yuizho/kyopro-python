N = int(input())
A, B, C = map(int, input().split())

result = 10**18
for i in range(9999 + 1):
    for j in range(9999 + 1 - i):
        tmp = N - (A * i + B * j)
        if tmp >= 0 and tmp % C == 0:
            k = tmp // C
            result = min(result, i + j + k)

print(result)
