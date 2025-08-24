S = input()
N = len(S)
ans = [0] * N

# Rの連続を数える
right_counts = [0] * N
count = 0
for i in range(N):
    if S[i] == "R":
        count += 1
    else:
        count = 0
    right_counts[i] = count

# print(right_counts)

# Lの連続を数える（右から）
left_counts = [0] * N
count = 0
for i in range(N - 1, -1, -1):
    if S[i] == "L":
        count += 1
    else:
        count = 0
    left_counts[i] = count

# print(left_counts)

# 子どもたちを分配する
for i in range(N - 1):
    if S[i] == "R" and S[i + 1] == "L":
        # Rブロックの人数
        r_len = right_counts[i]
        # Lブロックの人数
        l_len = left_counts[i + 1]

        # Rのマス(i)に集まる人数
        ans[i] = (r_len + 1) // 2 + l_len // 2  # ceil(r_len/2) + floor(l_len/2)
        # Lのマス(i+1)に集まる人数
        ans[i + 1] = r_len // 2 + (l_len + 1) // 2  # floor(r_len/2) + ceil(l_len/2)

print(*ans)
