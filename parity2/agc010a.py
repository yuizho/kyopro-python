N = int(input())

A = list(map(int, input().split()))

odds = [a for a in A if a % 2 != 0]

if len(odds) % 2 == 0:
    print("YES")
else:
    print("NO")
