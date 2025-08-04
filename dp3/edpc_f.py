s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_s + 1) for _ in range(len_t + 1)]

for i in range(1, len_t + 1):
    for j in range(1, len_s + 1):
        if t[i - 1] == s[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # print(dp[i])

lcs = ""
i = len_t
j = len_s

while 0 < i and 0 < j:
    if t[i - 1] == s[j - 1]:
        lcs = t[i - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(lcs)
