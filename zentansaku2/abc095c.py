A, B, C, X, Y = map(int, input().split())

ans = 10**30
for k in range(0, max(X, Y) + 1):
    a_amount = A * max(0, X - k)
    b_amount = B * max(0, Y - k)
    c_amount = 2 * C * k
    ans = min(ans, a_amount + b_amount + c_amount)

print(ans)
