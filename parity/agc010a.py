N = int(input())
A = list(map(int, input().split()))

odd = 0
even = 0
for i in range(N):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if odd % 2 == 0:
    print("YES")
else:
    print("NO")
