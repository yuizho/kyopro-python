#  https://atcoder.jp/contests/abc064/tasks/abc064_a

r, g, b = map(int, input().split())

if int(f"{r}{g}{b}") % 4 == 0:
    print("YES")
else:
    print("NO")
