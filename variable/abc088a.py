# https://atcoder.jp/contests/abc088/tasks/abc088_a

n = int(input())
a = int(input())

remain = n - ((n // 500) * 500)
if remain <= a:
    print("Yes")
else:
    print("No")
