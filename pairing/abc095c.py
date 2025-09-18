A, B, C, X, Y = map(int, input().split())

result1 = A * X + B * Y

result2 = C * min(X, Y) * 2
if X > Y:
    result2 += A * (X - Y)
elif X < Y:
    result2 += B * (Y - X)

result3 = C * max(X, Y) * 2

print(min(result1, result2, result3))
