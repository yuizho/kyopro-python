N = int(input())
coins = list(map(int, input().split()))

coins = sorted(coins, reverse=True)

result = 9999
for a in range(0, 10000):
    A = coins[0] * a
    if A > N:
        break
    for b in range(0, 10000 - a):
        B = coins[1] * b
        if A + B > N:
            break
        if (N - A - B) % coins[2] == 0:
            c = (N - A - B) // coins[2]
            result = min(result, a + b + c)

print(result)
