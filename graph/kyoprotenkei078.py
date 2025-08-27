N, M = map(int, input().split())
A: list[list[int]] = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a > b:
        A[a].append(b)
    elif b > a:
        A[b].append(a)

# print(A)
print(len(list(filter(lambda x: len(x) == 1, A))))
