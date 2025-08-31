def sieve_of_eratosthenes(n):
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


Q = int(input())

max_length = 10**5
sosu_set = set(sieve_of_eratosthenes(max_length + 2))
cum_sum = [0] * (max_length + 1)
for i in range(1, max_length + 1):
    cum_sum[i] = cum_sum[i - 1]
    if i % 2 != 0 and i in sosu_set and (i + 1) // 2 in sosu_set:
        cum_sum[i] += 1

for _ in range(Q):
    l, r = map(int, input().split())
    print(cum_sum[r] - cum_sum[l - 1])
