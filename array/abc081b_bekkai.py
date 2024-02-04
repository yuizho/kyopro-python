import itertools


def how_many_times(num: int) -> int:
    for i in itertools.count():
        if num % 2 == 0:
            num //= 2
        else:
            return i
    return 0


N = int(input())
A = list(map(int, input().split()))

print(min(map(how_many_times, A)))
