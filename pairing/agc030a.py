A, B, C = map(int, input().split())

result = B
if A + B < C:
    if C - (A + B) % 2 == 0:
        result += A + B
    else:
        result += A + B + 1
else:
    result += C

print(result)
