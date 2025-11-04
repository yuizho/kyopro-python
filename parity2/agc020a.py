N, A, B = map(int, input().split())

current_a = A
current_b = B

for _ in range(100):
    if current_a + 1 == current_b:
        print("Borys")
        exit()
    current_a += 1

    if current_b - 1 == current_a:
        print("Alice")
        exit()
    current_b -= 1

print(-1)
