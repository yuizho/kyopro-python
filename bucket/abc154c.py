from collections import Counter


N = int(input())
numbers = list(map(int, input().split()))

if all([v == 1 for v in Counter(numbers).values()]):
    print("YES")
else:
    print("NO")
