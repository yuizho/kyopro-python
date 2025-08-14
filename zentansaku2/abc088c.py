grid = [list(map(int, input().split())) for _ in range(3)]

result: list[list[tuple[int, int, int]]] = [[], [], []]
for i in range(3):
    for ai in range(max(grid[i]) + 1):
        for b1 in range(grid[i][0] + 1):
            for b2 in range(grid[i][1] + 1):
                for b3 in range(grid[i][2] + 1):
                    if (
                        grid[i][0] == ai + b1
                        and grid[i][1] == ai + b2
                        and grid[i][2] == ai + b3
                    ):
                        result[i].append((b1, b2, b3))

for r in result[0]:
    if r in result[1] and r in result[2]:
        print("Yes")
        exit()

print("No")
