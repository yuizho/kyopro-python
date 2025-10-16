N = int(input())
S = input()

cum_east = [0] * (N + 1)
cum_west = [0] * (N + 1)

for i in range(1, N + 1):
    cum_east[i] = cum_east[i - 1]
    cum_west[i] = cum_west[i - 1]
    if S[i - 1] == "E":
        cum_east[i] += 1
    else:
        cum_west[i] += 1

# print(cum_east)
# print(cum_west)

result = 10**18
for i in range(1, N + 1):
    left = cum_west[i - 1]
    right = cum_east[N] - cum_east[i]
    result = min(left + right, result)

print(result)
