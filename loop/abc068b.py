# https://atcoder.jp/contests/abc068/tasks/abc068_b

N = int(input())

ans = 1
max_count = 0
for num in range(1, N + 1):
    n = num
    count = 0
    while True:
        if n == 0:
            break
        if n % 2 == 0:
            count += 1
        n = n // 2
    if max_count < count:
        max_count = count
        ans = num


print(ans)
