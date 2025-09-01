x = int(input())

result = (x // 11) * 2
if x % 11 == 0:
    pass
elif x % 11 <= 6:
    result += 1
else:
    result += 2

print(result)
