# https://atcoder.jp/contests/abc220/tasks/abc220_b

K = int(input())
A, B = map(int, input().split())

print(int(str(A), K) * int(str(B), K))
