N = int(input())
S = input()

result = 0
for i in range(1, N):
    a = S[:i]
    b = S[i:]
    # print(i, a, b)
    result = max(result, len(set(a) & set(b)))

print(result)
