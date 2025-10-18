def calc_kitaichi(n):
    result = 0
    for i in range(1, n + 1):
        result += i * (1 / n)
    return result


N, K = map(int, input().split())
P = list(map(int, input().split()))

cum = [0] * (N + 1)
for i in range(1, N + 1):
    cum[i] = calc_kitaichi(P[i - 1]) + cum[i - 1]

result = 0
for i in range(K, N + 1):
    result = max(result, cum[i] - cum[i - K])

print(result)
