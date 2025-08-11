N, Y = map(int, input().split())

for i in range(N + 1):
    zankin1 = Y - 10000 * i
    if zankin1 < 0:
        break
    if zankin1 == 0 and i == N:
        print(i, 0, 0)
        exit()

    for j in range(N - i + 1):
        zankin2 = zankin1 - 5000 * j
        if zankin2 < 0:
            break
        k = zankin2 // 1000
        if i + j + k == N:
            print(i, j, k)
            exit()

print(-1, -1, -1)
