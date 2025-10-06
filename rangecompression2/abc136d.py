S = input()
N = len(S)
result = [0] * N

i = 0
while i < N - 1:
    if S[i] == "R" and S[i + 1] == "L":
        # Rブロックの長さを数える
        r = 0
        j = i
        while j >= 0 and S[j] == "R":
            r += 1
            j -= 1
        # Lブロックの長さを数える
        l = 0
        k = i + 1
        while k < N and S[k] == "L":
            l += 1
            k += 1
        # 集まる位置に人数を割り当てる
        result[i] = (r + 1) // 2 + l // 2
        result[i + 1] = r // 2 + (l + 1) // 2
        i = k  # 次の未処理区間へ
    else:
        i += 1

print(" ".join(map(str, result)))
