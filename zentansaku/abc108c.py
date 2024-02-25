import itertools


N, K = map(int, input().split())

str_suuretsu = "".join(map(str, range(1, N + 1)))
kumiawase = itertools.product(str_suuretsu, repeat=3)

result = 0
for k in kumiawase:
    a = int(k[0])
    b = int(k[1])
    c = int(k[2])
    if (a + b) % K == 0 and (b + c) % K == 0 and (c + a) % K == 0:
        result += 1

print(result)
