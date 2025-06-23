N = int(input())


def create_josu_list(n: int) -> list[int]:
    result: list[int] = []
    for i in range(1, N):
        josu = n**i
        if josu > N:
            return result
        result.append(josu)
    return result


ONE = 1
SIX = create_josu_list(6)
NINE = create_josu_list(9)

INF = 10**18

dp = [INF] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    if i - 1 >= 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for s in SIX:
        if i - s < 0:
            break
        dp[i] = min(dp[i], dp[i - s] + 1)
    for n in NINE:
        if i - n < 0:
            break
        dp[i] = min(dp[i], dp[i - n] + 1)

print(dp[N])
