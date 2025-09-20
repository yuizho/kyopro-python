Q, H, S, D = map(int, input().split())
N = int(input())

min_1_l = min(Q * 4, H * 2, S)
min_2_l = min(min_1_l * 2, D)

# print(min_1_l, min_2_l)

if N == 1:
    print(min_1_l)
else:
    result = N // 2 * min_2_l
    if N % 2 != 0:
        result += min_1_l
    print(result)
