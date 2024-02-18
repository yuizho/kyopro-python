# https://atcoder.jp/contests/past202004-open/tasks/past202004_c

N = int(input())


table = [list(input()) for _ in range(N)]

for i in range(N - 1, -1, -1):
    for j in range(2 * N - 1):
        if table[i][j] == "#":
            if i < N - 1 and j > 0:
                if table[i + 1][j - 1] == "X":
                    table[i][j] = "X"
            if i < N - 1 and j < 2 * N - 2:
                if table[i + 1][j + 1] == "X":
                    table[i][j] = "X"
            if i < N - 1:
                if table[i + 1][j] == "X":
                    table[i][j] = "X"

for r in table:
    for c in r:
        print(c, end="")
    print()
