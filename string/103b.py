S = input()
T = input()

for _ in S:
    S = S[-1] + S[0:-1]
    if S == T:
        print("Yes")
        exit()
print("No")
