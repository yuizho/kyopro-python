# https://atcoder.jp/contests/abc158/tasks/abc158_c

A, B = map(int, input().split())


result = -1
for i in range(1, 1001):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        result = i
        break

print(result)
