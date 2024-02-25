N = int(input())
S = input()

result = 0
for n in range(1, N):
    result = max(len(set(S[0:n]) & set(S[n:])), result)

print(result)
