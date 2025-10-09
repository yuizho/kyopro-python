import collections


N = int(input())
A = list(map(int, input().split()))

staffs: dict[int, int] = collections.defaultdict(int)

for a in A:
    staffs[a - 1] += 1

for i in range(N):
    print(staffs[i])
