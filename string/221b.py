S = input()
T = input()

if S == T:
    print("Yes")
    exit()

s = list(S)

for i in range(1, len(S)):
    s = list(S)
    s[i], s[i - 1] = s[i - 1], s[i]
    if s == list(T):
        print("Yes")
        exit()

print("No")
