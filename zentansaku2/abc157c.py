N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(M)]

# N桁の数値 (先頭0はだめ)
# すべての条件(si桁目の数字がci)を満たす整数のうち最小のものを探す

result = -1
for i in range(0, 10**N):
    s = f"{i:0{N}d}"
    if N >= 2 and s[0] == "0":
        continue
    ok = True
    for pos, c in conditions:
        if s[pos - 1] != str(c):
            ok = False
            break
    if ok:
        result = i
        break

print(result)
