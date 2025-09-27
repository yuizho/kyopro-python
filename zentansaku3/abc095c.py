A, B, C, X, Y = map(int, input().split())


result1 = A * X + B * Y
result2 = C * max(X, Y) * 2
result3 = C * Y * 2 + (X - Y) * A if X > Y else C * X * 2 + (Y - X) * B

print(min(result1, result2, result3))
