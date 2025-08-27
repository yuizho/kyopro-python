N, M = map(int, input().split())
A: list[list[int]] = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 効率のため目的地から探るようにする
    A[b].append(a)

step1 = A[N - 1]
for i in step1:
    if 0 in A[i]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
