N = int(input())
A = [int(input()) for _ in range(N)]

reached = [False] * N

current_button = 1
count = 0

for i in range(N):
    count += 1

    if reached[current_button - 1]:
        print(-1)
        exit()

    reached[current_button - 1] = True
    current_button = A[current_button - 1]

    if current_button == 2:
        print(count)
        exit()

print(-1)
