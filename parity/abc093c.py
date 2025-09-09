A, B, C = map(int, input().split())

a_mod = A % 2
b_mod = B % 2
c_mod = C % 2

result = 0
if not a_mod == b_mod == c_mod:
    result += 1
    if a_mod == b_mod:
        A += 1
        B += 1
    elif b_mod == c_mod:
        B += 1
        C += 1
    elif a_mod == c_mod:
        A += 1
        C += 1

# print(A, B, C)

for _ in range(100):
    if A == B == C:
        break

    result += 1
    if A <= B and A <= C:
        A += 2
    elif B <= A and B <= C:
        B += 2
    elif C <= A and C <= B:
        C += 2

print(result)
