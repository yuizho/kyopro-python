from collections import Counter


N = int(input())
votes = [input() for _ in range(N)]

counter = Counter(votes)
max_count = max(counter.values())
result = []
for k, v in counter.items():
    if v == max_count:
        result.append(k)

for r in sorted(result):
    print(r)
