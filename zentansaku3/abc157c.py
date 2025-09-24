N, M = map(int, input().split())

values = set([])
for i in range(M):
    s, c = map(int, input().split())
    values.add((s, c))

if len(list(map(lambda x: x[0], values))) != len(set(map(lambda x: x[0], values))):
    print(-1)
    exit()

result = [0] * N
if N > 1:
    result[0] = 1

for s, c in values:
    result[s - 1] = c

if result[0] == 0 and N > 1:
    print(-1)
else:
    print("".join(map(str, result)))
