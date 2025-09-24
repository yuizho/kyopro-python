N = int(input())
A, B, C = map(int, input().split())

result = 10**18
for i in range(10000):
    for j in range(10000 - i):
        if (N - (A * i + B * j)) % C == 0:
            k = (N - (A * i + B * j)) // C
            if k < 0:
                break
            result = min(result, i + j + k)

print(result)
