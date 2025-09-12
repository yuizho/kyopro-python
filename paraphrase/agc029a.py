S = input()

if "BW" not in S:
    print(0)
    exit()

left = 0
result = 0
for i in range(len(S)):
    if S[i] == "W":
        result += i - left
        left += 1

print(result)
