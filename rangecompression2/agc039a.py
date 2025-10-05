S = input()
K = int(input())
N = len(S)

if len(set(S)) == 1:
    # 全体で1つの巨大なブロックとして計算
    ans = (N * K) // 2
    print(ans)
    exit()

single_needs_replacing = 0
i = 0
while i < N:
    j = i

    while j < N and S[i] == S[j]:
        j += 1

    single_needs_replacing += (j - i) // 2

    i = j

double_needs_replacing = 0
SS = S + S
NN = len(SS)
i = 0
while i < NN:
    j = i

    while j < NN and SS[i] == SS[j]:
        j += 1

    double_needs_replacing += (j - i) // 2

    i = j

# print(single_needs_replacing, double_needs_replacing)

diff = double_needs_replacing - single_needs_replacing
if diff == 0:
    print(K * single_needs_replacing)
else:
    print((K - 1) * diff + single_needs_replacing)
