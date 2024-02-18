card = [
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
]

N = int(input())
numbers = [int(input()) for _ in range(N)]

for r in range(3):
    for c in range(3):
        if card[r][c] in numbers:
            card[r][c] = 1
        else:
            card[r][c] = 0

# check
zipped = list(zip(*card))
for i in range(3):
    if all(card[i]):
        print("Yes")
        exit()
    if all(zipped[i]):
        print("Yes")
        exit()

if all([card[0][0], card[1][1], card[2][2]]) or all(
    [card[0][2], card[1][1], card[2][0]]
):
    print("Yes")
    exit()

print("No")
