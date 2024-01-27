# https://atcoder.jp/contests/abc090/tasks/abc090_b

A, B = map(int, input().split())


def calc_sum_digits(n: int) -> int:
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit


result = 0
for number in range(A, B + 1):
    if str(number) == str(number)[::-1]:
        result += 1

print(result)
