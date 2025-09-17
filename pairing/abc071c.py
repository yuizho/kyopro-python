import collections


N = int(input())
A = list(map(int, input().split()))

match_by_counts = collections.Counter(A)
# print(match_by_counts)

top = 0
top_count = 0
second = 0
second_count = 0

for num, count in match_by_counts.items():
    if count < 2:
        continue

    if top < num:
        second = top
        second_count = top_count
        top = num
        top_count = count
    elif second < num:
        second = num
        second_count = count

# print(top, top_count)
# print(second, second_count)

if top_count >= 4:
    print(top * top)
else:
    print(top * second)
