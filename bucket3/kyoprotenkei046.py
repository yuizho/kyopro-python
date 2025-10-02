from collections import Counter


N = int(input())
A = Counter(map(lambda x: int(x) % 46, input().split()))
B = Counter(map(lambda x: int(x) % 46, input().split()))
C = Counter(map(lambda x: int(x) % 46, input().split()))

# print(A, B, C)

result = 0
for an, ac in A.items():
    for bn, bc in B.items():
        for cn, cc in C.items():
            if (an + bn + cn) % 46 == 0:
                result += ac * bc * cc

print(result)
