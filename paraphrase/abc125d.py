N = int(input())
A = list(map(int, input().split()))

abs_min = 10**18
negative_count = 0
for i in range(N):
    if A[i] < 0:
        negative_count += 1
    abs_min = min(abs_min, abs(A[i]))

result = sum(map(abs, A))
if negative_count % 2 != 0:
    result -= abs_min * 2
print(result)
