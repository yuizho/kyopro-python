a, b = map(int, input().split())

if a < 0 and b > 0 or a == 0 or b == 0:
    print("Zero")
    exit()


if a < 0 and b < 0:
    if len(range(a, b + 1)) % 2 == 0:
        print("Positive")
    else:
        print("Negative")

    exit()

print("Positive")
