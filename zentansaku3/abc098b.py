N = int(input())
S = input()

result = 0
for i in range(1, N):
    a = set(S[i:])
    b = set(S[:i])

    # print(a & b)
    result = max(result, len(a & b))

print(result)
