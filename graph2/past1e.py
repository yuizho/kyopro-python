N, Q = map(int, input().split())

follows: list[set[int]] = [set() for _ in range(N)]
followers: list[set[int]] = [set() for _ in range(N)]

for _ in range(Q):
    t, *ops = map(int, input().split())
    a = ops[0] - 1

    if t == 1:
        b = ops[1] - 1
        follows[a].add(b)
        followers[b].add(a)
    elif t == 2:
        for x in followers[a]:
            follows[a].add(x)
            followers[x].add(a)
    else:
        follows_tmp = set()
        for x in follows[a]:
            for xx in follows[x]:
                if xx != a:
                    follows_tmp.add(xx)
                    followers[xx].add(a)
        follows[a].update(follows_tmp)

# print(follows)
# print(followers)

for follow in follows:
    result = ["N"] * N
    for f in follow:
        result[f] = "Y"
    print("".join(result))
