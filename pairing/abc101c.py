N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1
remaining = len(A) - K
result += (remaining + K - 2) // (K - 1)

print(result)
