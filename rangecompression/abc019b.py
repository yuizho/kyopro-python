S = input()
S_size = len(S)

result = ""
i = 0
while i < S_size:
    j = i
    while j < S_size and S[j] == S[i]:
        j += 1

    result += S[i:j][0] + str(len(S[i:j]))

    i = j

print(result)
