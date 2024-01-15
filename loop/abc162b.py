N = int(input())

result = 0
for n in range(1, N + 1):
    if not n % 3 == 0 and not n % 5 == 0:
        result += n

print(result)
