A, B, C = map(int, input().split())

cycles = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

d = A % 10
cycle = cycles[d]
L = len(cycle)

if L == 1:
    print(cycle[0])
else:
    e_mod = pow(B, C, L)  # E = B^C (mod L)
    idx = (e_mod - 1) % L  # 0 のときは L-1 扱い
    print(cycle[idx])
