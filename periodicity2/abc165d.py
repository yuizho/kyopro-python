A, B, N = map(int, input().split())

x = N if B > N else B - 1

print(A * x // B)
