A, B, C = map(int, input().split())

adjust = 0
if A % 2 == B % 2 != C % 2:
    A += 1
    B += 1
    adjust = 1
elif A % 2 != B % 2 == C % 2:
    B += 1
    C += 1
    adjust = 1
elif A % 2 == C % 2 != B % 2:
    A += 1
    C += 1
    adjust = 1

M = max(A, B, C)
diff_sum = (M - A) + (M - B) + (M - C)


print(diff_sum // 2 + adjust)
