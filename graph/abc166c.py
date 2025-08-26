N, M = map(int, input().split())
H = list(map(int, input().split()))

result = [True] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if H[A] <= H[B]:
        result[A] = False

    if H[A] >= H[B]:
        result[B] = False

print(sum(result))
