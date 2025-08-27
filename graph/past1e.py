N, Q = map(int, input().split())

# フォローしているユーザリスト
follows = [[False] * N for _ in range(N)]
# フォローされているユーザリスト
followers: list[set[int]] = [set() for _ in range(N)]

for _ in range(Q):
    t, a, *_b = map(int, input().split())
    a -= 1
    if t == 1:
        b = _b[0] - 1
        follows[a][b] = True
        followers[b].add(a)
    elif t == 2:
        for follower in followers[a]:
            follows[a][follower] = True
            followers[follower].add(a)
    else:
        needs_followings = []
        for x, v in enumerate(follows[a]):
            if not v:
                continue
            for xx, xv in enumerate(follows[x]):
                if not xv or xx == a:
                    continue
                needs_followings.append(xx)
        for x in needs_followings:
            follows[a][x] = True
            followers[x].add(a)


for f in follows:
    print("".join(map(lambda x: "Y" if x else "N", f)))
