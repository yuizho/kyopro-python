S = input()
T = input()


result = len(T)
for i in range(len(S) - len(T) + 1):
    needs_cange = 0
    for j, t in enumerate(T):
        if S[i + j] != t:
            needs_cange += 1
    result = min(result, needs_cange)

print(result)
