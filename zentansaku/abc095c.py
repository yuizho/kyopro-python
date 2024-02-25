A, B, C, X, Y = map(int, input().split())

result = 0
if A + B > C * 2:
    result = min(X, Y) * C * 2
    minus = min(X, Y)
    X = X - minus
    Y = Y - minus

if A > C * 2:
    result += C * 2 * X
else:
    result += A * X
if B > C * 2:
    result += C * 2 * Y
else:
    result += B * Y

print(result)
