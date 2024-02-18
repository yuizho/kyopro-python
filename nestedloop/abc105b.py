N = int(input())

for d_4 in range(50):
    for d_7 in range(50):
        if d_4 * 4 + d_7 * 7 == N:
            print("Yes")
            exit()

print("No")
