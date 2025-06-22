INF = 2**60

N = int(input())
h = list(map(int, input().split()))


def rec(i):
    if i == 0:
        return 0

    result = INF

    if i - 1 >= 0:
        result = min(result, rec(i - 1) + abs(h[i] - h[i - 1]))

    if i - 2 >= 0:
        result = min(result, rec(i - 2) + abs(h[i] - h[i - 2]))

    return result


print(rec(N - 1))
