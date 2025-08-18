S = input()
S_size = len(S)

words = []
i = 0
while i < S_size:
    j = i + 1
    word = S[i]
    while j < S_size and not S[j].isupper():
        word += S[j]
        j += 1
    word += S[j]
    words.append(word)

    i = j + 1

words.sort(key=str.lower)
print("".join(words))
