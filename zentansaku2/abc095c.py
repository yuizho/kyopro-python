A, B, C, X, Y = map(int, input().split())


amount1 = A * X + B * Y
amount2 = 2 * C * max(X, Y)

less_count = min(X, Y)
remaining_count = max(X, Y) - less_count
remaining_pizza = B if X < Y else A

amount3 = 2 * C * less_count + remaining_pizza * remaining_count

print(min(min(amount1, amount2), amount3))
