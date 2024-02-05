S = input()

for i in range(1, len(S) + 1):
    s = S[0:-i]

    if len(s) % 2 != 0:
        continue

    d = len(s) // 2
    if s[0:d] == s[d:]:
        print(len(s))
        exit()
