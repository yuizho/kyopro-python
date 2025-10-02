from collections import Counter


N = int(input())

counters = [Counter(input()) for _ in range(N)]
duplicates = counters[0]
for i in range(1, len(counters)):
    duplicates = duplicates & counters[i]

result = []
for s, count in duplicates.items():
    result.append(s * count)

result.sort()

print("".join(result))
