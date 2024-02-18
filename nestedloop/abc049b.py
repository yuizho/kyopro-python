H, W = map(int, input().split())
image = [input().split() for _ in range(H)]

expanded = []
for h in range(H):
    expanded.append(image[h])
    expanded.append(image[h])

for r in expanded:
    print("".join(r))
