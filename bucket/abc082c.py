from collections import Counter


N = int(input())
nums = list(map(int, input().split()))

counter = Counter(nums)

result = 0
for k, v in counter.items():
    if k > v:
        result += v
    if k < v:
        result += v - k

print(result)
