A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if a * 500 + b * 100 + c * 50 == X:
                result += 1

print(result)
