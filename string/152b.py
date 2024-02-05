a, b = map(int, input().split())

if str(a) * b > str(b) * a:
    print(str(b) * a)
else:
    print(str(a) * b)
