H, W = map(int, input().split())
field = []
for _ in range(H):
    field.append(list(input()))

converted = field
for h in range(H):
    for w in range(W):
        if field[h][w] == "#":
            converted[h][w] = "#"
            continue
        cnt = 0
        if h > 0:
            if converted[h - 1][w] == "#":
                cnt += 1
        if h < H - 1:
            if converted[h + 1][w] == "#":
                cnt += 1
        if w > 0:
            if converted[h][w - 1] == "#":
                cnt += 1
        if w < W - 1:
            if converted[h][w + 1] == "#":
                cnt += 1
        if h > 0 and w > 0:
            if converted[h - 1][w - 1] == "#":
                cnt += 1
        if h < H - 1 and w < W - 1:
            if converted[h + 1][w + 1] == "#":
                cnt += 1
        if h > 0 and w < W - 1:
            if converted[h - 1][w + 1] == "#":
                cnt += 1
        if h < H - 1 and w > 0:
            if converted[h + 1][w - 1] == "#":
                cnt += 1

        converted[h][w] = str(cnt)

for c in converted:
    print("".join(c))
