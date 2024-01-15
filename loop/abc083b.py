N, A, B = map(int, input().split())


def calc_sum_digits(n: int) -> int:
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit


result = 0
for n in range(1, N + 1):
    ns = calc_sum_digits(n)
    if A <= ns and B >= ns:
        result += n

print(result)
