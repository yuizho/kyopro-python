N, Y = map(int, input().split())

for man in range(N + 1):
    for gosen in range(N + 1):
        sen = N - man - gosen

        if sen < 0:
            continue

        if 10 * man + 5 * gosen + 1 * sen == Y // 1000 and man + gosen + sen == N:
            print(man, gosen, sen)
            exit()
print("-1 -1 -1")
