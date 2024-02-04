# https://atcoder.jp/contests/abc113/tasks/abc113_b

N = int(input())
T, A = map(int, input().split())
heights = map(int, input().split())

diffs = []
for height in heights:
    avg_tempreture = T * 1000 - height * 6
    diffs.append(abs(A * 1000 - avg_tempreture))

print(diffs.index(min(diffs)) + 1)
