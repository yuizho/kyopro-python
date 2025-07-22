from collections import Counter


N, K = map(int, input().split())
balls = map(int, input().split())

counter = Counter(balls)

if len(counter) <= K:
    print(0)
    exit(0)

result = 0
b = sorted(counter.values())
for i in range(len(counter) - K):
    result += b[i]

print(result)
