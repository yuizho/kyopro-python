N = int(input())
A = list(map(int, input().split()))

result = sum(sorted(A, reverse=True)[1 : 2 * N : 2])
print(result)
