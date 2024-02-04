# https://atcoder.jp/contests/abc205/tasks/abc205_b

N = int(input())
A = list(map(int, input().split()))

if sorted(A) == list(range(1, N + 1)):
    print("Yes")
else:
    print("No")
