S = input()

s = list(S)
result = 0
for i in range(len(s)):
    r = list(reversed(s))
    if s[i] != r[i]:
        result += 1
        s[i] = r[i]

print(result)
