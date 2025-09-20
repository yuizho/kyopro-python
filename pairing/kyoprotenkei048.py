N, K = map(int, input().split())
scores = []
for _ in range(N):
    a, b = map(int, input().split())
    scores.append(b)
    scores.append(a - b)

scores.sort(reverse=True)

result = 0
for i in range(K):
    result += scores[i]

print(result)
