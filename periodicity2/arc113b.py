A, B, C = map(int, input().split())

P = [
    [],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
]

tmp = int(str(A)[-1])
print((B % len(P[tmp])))

tmp = tmp ** (B % len(P[tmp]))
print(tmp)
print(P[tmp])

result = tmp ** (C % len(P[tmp]))
print(result)
