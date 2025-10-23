x = int(input())

result = (x // 11) * 2
if 1 <= x % 11 <= 6:
    result += 1
elif 7 <= x % 11 <= 11:
    result += 2

print(result)
