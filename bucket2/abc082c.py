import collections


N = int(input())
numbers = list(map(int, input().split()))

nums_by_count = collections.Counter(numbers)

result = 0
for num, count in nums_by_count.items():
    if count > num:
        result += count - num
    elif count < num:
        result += count

print(result)
