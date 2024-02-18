# https://atcoder.jp/contests/past202010-open/tasks/past202010_c

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        cnt = 0
        if table[i][j] == "#":
            cnt += 1
        if i > 0:
            if table[i - 1][j] == "#":
                cnt += 1
            if j > 0:
                if table[i - 1][j - 1] == "#":
                    cnt += 1
            if j < M - 1:
                if table[i - 1][j + 1] == "#":
                    cnt += 1
        if i < N - 1:
            if table[i + 1][j] == "#":
                cnt += 1
            if j > 0:
                if table[i + 1][j - 1] == "#":
                    cnt += 1
            if j < M - 1:
                if table[i + 1][j + 1] == "#":
                    cnt += 1
        if j > 0:
            if table[i][j - 1] == "#":
                cnt += 1
        if j < M - 1:
            if table[i][j + 1] == "#":
                cnt += 1
        print(cnt, end="")
    print("")
