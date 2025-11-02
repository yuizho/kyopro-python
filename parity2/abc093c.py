A, B, C = map(int, input().split())

if A == B == C:
    print(0)
    exit()

is_a_even = A % 2 - -0
is_b_even = B % 2 - -0
is_c_even = C % 2 - -0

result = 0
if is_a_even == is_b_even != is_c_even:
    result += 1
    A += 1
    B += 1
elif is_a_even != is_b_even == is_c_even:
    result += 1
    B += 1
    C += 1
elif is_a_even == is_c_even != is_b_even:
    result += 1
    A += 1
    C += 1

max_num = max(A, B, C)
diff = max_num - A
diff += max_num - B
diff += max_num - C

result += diff // 2
print(result)
