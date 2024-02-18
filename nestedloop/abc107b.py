H, W = map(int, input().split())
table = [list(input()) for _ in range(H)]

deleted = []
for i in range(H):
    if "#" in table[i]:
        deleted.append(table[i])

zipped = list(zip(*deleted))
result = []
for i in range(W):
    if "#" in zipped[i]:
        result.append(zipped[i])

for r in zip(*result):
    print("".join(r))
