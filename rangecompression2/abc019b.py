S = input()
N = len(S)

i = 0
result = ""
while i < N:
    j = i
    while j < N and S[j] == S[i]:
        j += 1

    result += f"{S[i]}{j - i}"

    i = j

print(result)
