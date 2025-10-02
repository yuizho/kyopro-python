from collections import Counter


N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
# print(counter)

result = 0
for num, count in counter.items():
    if count < num:
        result += count
    elif num < count:
        result += count - num

print(result)
