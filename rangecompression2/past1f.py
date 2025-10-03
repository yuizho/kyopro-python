S = input()

S_size = len(S)
words = []
i = 0
while i < S_size:
    j = i + 1

    while j < S_size and S[j].islower():
        j += 1

    words.append(S[i : j + 1])

    i = j + 1

print("".join(sorted(words, key=str.lower)))
