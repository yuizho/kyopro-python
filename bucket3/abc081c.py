from collections import Counter


N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = Counter(A)
result = sum(sorted(counter.values(), reverse=True)[K:])
print(result)
