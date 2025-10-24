import sys

N, K = map(int, input().split())
# 0-indexedに直しておく (1番の町はindex 0)
A = list(map(int, input().split()))
A = [x - 1 for x in A]

# visited[i] = k は、町i+1にkステップ目に到達したことを示す
# 未到達は-1で初期化
visited = [-1] * N
# 実際に通った経路(1-indexed)を記録するリスト
path = []

current_town = 0  # 0-indexedで町を管理
step = 0

while visited[current_town] == -1:
    visited[current_town] = step
    path.append(current_town + 1)  # 答えは1-indexedなので+1して記録
    current_town = A[current_town]
    step += 1

# ループを検出した時点で...
# current_town はループの開始地点
# step は ループ開始地点に2回目に来たステップ数
# visited[current_town] は ループ開始地点に1回目に来たステップ数

tail_len = visited[current_town]
loop_len = step - tail_len

if K < tail_len:
    # 場合1: Kがしっぽの長さより短い
    print(path[K])
else:
    # 場合2: Kがループに到達する
    remaining_K = K - tail_len
    loop_index = remaining_K % loop_len

    # ループ部分の経路だけを切り出す
    loop_path = path[tail_len:]

    print(loop_path[loop_index])
