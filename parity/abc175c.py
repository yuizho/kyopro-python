X, K, D = map(int, input().split())

X = abs(X)

if X // D >= K:
    print(X - K * D)
    exit()

moves_to_zero = X // D
remaining_k = K - moves_to_zero

if remaining_k % 2 == 0:
    print(X % D)
else:
    print(abs(X % D - D))
