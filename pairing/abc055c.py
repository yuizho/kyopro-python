N, M = map(int, input().split())

if M < 2:
    print(0)
elif N == 0:
    print(M // 4)
elif N > M // 2:
    print(M // 2)
else:
    result = N
    M -= 2 * N
    result += M // 4
    print(result)
