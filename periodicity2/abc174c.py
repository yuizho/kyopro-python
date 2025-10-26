K = int(input())

# 7, 77, 777, ... の K で割った余りを計算していく
rem = 0
count = 0

# K回試せば十分（K+1回目には必ずループに入るため）
for i in range(1, K + 1):
    count += 1

    # rem = (rem * 10 + 7) % K
    # この計算で、常に rem は K より小さい値に保たれる
    rem = (rem * 10 + 7) % K

    # 余りが0になったら、その時点の桁数 i が答え
    if rem == 0:
        print(count)
        exit()  # プログラムを終了

# ループが K 回終わっても見つからなければ、答えは存在しない
print(-1)
