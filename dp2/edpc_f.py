s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs = ""
i = len_s
j = len_t

while 0 < i and 0 < j:
    if s[i - 1] == t[j - 1]:
        lcs = s[i - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i - 1][j] < dp[i][j - 1]:
        j -= 1
    else:
        i -= 1

print(lcs)
