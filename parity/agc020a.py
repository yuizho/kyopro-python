N, A, B = map(int, input().split())

distance = B - A
if distance % 2 == 0:
    print("Alice")
else:
    print("Borys")
