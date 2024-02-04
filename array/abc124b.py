# https://atcoder.jp/contests/abc124/tasks/abc124_b

N = int(input())
mountains = list(map(int, input().split()))

result = 1
biggest = mountains[0]

for m in mountains[1:]:
    if m >= biggest:
        result += 1
        biggest = m

print(result)
