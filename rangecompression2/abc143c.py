N = int(input())
S = input()

i = 0
result = 0
while i < len(S):
    j = i
    while j < len(S) and S[j] == S[i]:
        j += 1

    result += 1

    i = j

print(result)
