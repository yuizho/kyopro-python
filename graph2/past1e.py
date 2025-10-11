N, Q = map(int, input().split())

follows: list[list[int]] = [[] for _ in range(N)]
followers: list[list[int]] = [[] for _ in range(N)]

for _ in range(Q):
    t, *ops = map(int, input().split())
    a = ops[0] - 1

    if t == 1:
        b = ops[1] - 1
        follows[a].append(b)
        followers[b].append(a)
    elif t == 2:
        for x in followers[a]:
            follows[a].append(x)
            followers[x].append(a)
    else:
        follows_tmp = []
        for x in follows[a]:
            for xx in follows[x]:
                follows_tmp.append(xx)
                followers[xx].append(a)
        follows[a] += follows_tmp

# print(follows)
# print(followers)

for follow in follows:
    result = ["N"] * N
    for f in follow:
        result[f] = "Y"
    print("".join(result))
