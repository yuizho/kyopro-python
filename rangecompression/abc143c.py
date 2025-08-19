N = int(input())
S = input()
S_size = len(S)

i = 0
result = 0
while i < S_size:
    j = i
    while j < S_size and S[j] == S[i]:
        j += 1

    result += 1

    i = j

print(result)
