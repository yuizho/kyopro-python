def create_sosu_list(n):
    primes = [True] * (n + 1)  # n+1 のサイズのブーリアンリストを作成
    primes[0] = primes[1] = False  # 0 と 1 は素数ではない

    # 2から√nまでをチェック
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            # pの倍数をすべて消す
            for i in range(p * p, n + 1, p):
                primes[i] = False

    # 素数のみをリストに格納
    return [p for p, is_prime in enumerate(primes) if is_prime]


N = int(input())
sosu_list = set(create_sosu_list(10**5))
cum = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    cum[i] = cum[i - 1]
    if i in sosu_list and (i + 1) // 2 in sosu_list:
        cum[i] += 1

for _ in range(N):
    left, right = map(int, input().split())
    print(cum[right] - cum[left - 1])
