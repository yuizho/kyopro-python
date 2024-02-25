import itertools


N, P, Q = map(int, input().split())
S = list(map(int, input().split()))

result = 0
for a, b, c, d, e in itertools.combinations(S, 5):
    if a % P * b % P * c % P * d % P * e % P == Q:
        result += 1

print(result)
