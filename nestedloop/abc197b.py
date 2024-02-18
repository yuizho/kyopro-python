H, W, X, Y = map(int, input().split())
table = [list(input()) for _ in range(H)]

x = Y - 1
y = X - 1

# 自分を含む
result = 1
for i in range(1, x + 1):
    if table[y][x - i] == ".":
        result += 1
    else:
        break

for i in range(1, W - x):
    if table[y][x + i] == ".":
        result += 1
    else:
        break

for i in range(1, y + 1):
    if table[y - i][x] == ".":
        result += 1
    else:
        break

for i in range(1, H - y):
    if table[y + i][x] == ".":
        result += 1
    else:
        break

print(result)
