A, B, C = map(int, input().split())

P = [
    [0],
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

a = A % 10
cycle = P[a]
L = len(cycle)

if L == 1:
    print(cycle[0])
else:
    e_mod = pow(B, C, L)  # B ** C % L
    print(cycle[e_mod - 1])
