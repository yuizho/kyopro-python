N, K = map(int, input().split())
S = input()

# 1. まず、現在の幸福度を計算する
happy_count = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        happy_count += 1

# 2. K回の操作で増やせる幸福度は最大で 2*K
increase = 2 * K

# 3. 合計する
potential_happy = happy_count + increase

# 4. 上限(N-1)を超えないようにする
ans = min(potential_happy, N - 1)

print(ans)
