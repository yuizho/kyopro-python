N = int(input())
mojis = [input() for _ in range(N)]

kami = set([])
for moji in mojis:
    if moji not in kami:
        kami.add(moji)
    else:
        kami.remove(moji)

print(len(kami))
