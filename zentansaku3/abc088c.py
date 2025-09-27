grid = [list(map(int, input().split())) for _ in range(3)]

A_max_candidates = [0] * 3
for i in range(3):
    A_max_candidates[i] = min(grid[i])

result = [False] * 3
for i in range(3):
    a1 = A_max_candidates[0]
    a2 = A_max_candidates[1]
    a3 = A_max_candidates[2]

    if grid[0][i] - a1 == grid[1][i] - a2 == grid[2][i] - a3:
        result[i] = True

print("No" if False in result else "Yes")
