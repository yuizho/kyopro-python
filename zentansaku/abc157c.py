import itertools


N, M = map(int, input().split())
SC = {tuple(map(int, input().split())) for _ in range(M)}

Num = map(
    lambda x: str(int("".join(x))),
    itertools.product("0123456789", repeat=N),
)

for num in Num:
    if len(num) != N:
        continue
    ok = True
    for sc in SC:
        if num[sc[0] - 1] != str(sc[1]):
            ok = False
            break
    if ok:
        print(num)
        exit(0)

print(-1)
