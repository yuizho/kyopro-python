N, K = map(int, input().split())
A = list(map(int, input().split()))

reached = [False] * N
reached[0] = True

reached_towns = [1]

next_town = A[0]
for i in range(0, N):
    reached_towns.append(next_town)
    if reached[next_town - 1]:
        break
    reached[next_town - 1] = True
    next_town = A[next_town - 1]

# print(reached_towns)


reached1 = reached_towns[: reached_towns.index(reached_towns[-1])]
if len(reached1) > K:
    print(reached_towns[K])
    exit()

K -= len(reached1)

reached2 = reached_towns[len(reached1) : -1]
print(reached2[K % len(reached2)])
