X = int(input())

result = 1
for i in range(2, X + 1):
    tmp = i * i
    while tmp <= X:
        result = max(result, tmp)
        tmp *= i

print(result)
