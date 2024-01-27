# https://atcoder.jp/contests/abc206/tasks/abc206_b

N = int(input())

day = 0
saved = 0
while N > saved:
    day += 1
    saved += day

print(day)
