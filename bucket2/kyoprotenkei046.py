N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Step 1: 余りごとの個数を数える
# 長さ46のリストを0で初期化
countA = [0] * 46
countB = [0] * 46
countC = [0] * 46

for i in range(N):
    countA[A[i] % 46] += 1
    countB[B[i] % 46] += 1
    countC[C[i] % 46] += 1

# 答えを格納する変数
ans = 0

# Step 2: 余りの組み合わせを全探索
for rA in range(46):
    for rB in range(46):
        for rC in range(46):
            # 余りの合計が46の倍数になるかチェック
            if (rA + rB + rC) % 46 == 0:
                # 条件を満たすなら、その組み合わせの総数を答えに足す
                ans += countA[rA] * countB[rB] * countC[rC]

print(ans)
