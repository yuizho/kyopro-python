N = int(input())
S = input()

cum_sum_w = [0] * (N + 1)
cum_sum_e = [0] * (N + 1)
for i in range(1, N + 1):
    cum_sum_w[i] = cum_sum_w[i - 1]
    cum_sum_e[i] = cum_sum_e[i - 1]
    if S[i - 1] == "W":
        cum_sum_w[i] += 1
    else:
        cum_sum_e[i] += 1

# print(cum_sum_w)
# print(cum_sum_e)

result = 10**18
for i in range(1, N + 1):
    needs_changing = cum_sum_w[i - 1]
    if i < N:
        l = i
        r = N
        needs_changing += cum_sum_e[r] - cum_sum_e[l]
    result = min(result, needs_changing)

print(result)
