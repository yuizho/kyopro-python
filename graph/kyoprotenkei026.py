import sys
from collections import deque

# 高速な入力を受け取る
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 頂点の色を格納する配列 (-1:未訪問, 0:白, 1:黒)
colors = [-1] * N

# --- ここからBFSでの二色塗り ---
# BFSで使うキューを用意
q = deque()

# 始点となる頂点0をキューに入れ、色を白(0)で塗る
q.append(0)
colors[0] = 0

# キューが空になるまでループ
while q:
    # キューの先頭から頂点を取り出す
    v = q.popleft()

    # 取り出した頂点vに隣接する頂点を調べる
    for next_v in graph[v]:
        # まだ塗られていなければ
        if colors[next_v] == -1:
            # vと反対の色で塗り、キューに追加する
            colors[next_v] = 1 - colors[v]
            q.append(next_v)
# --- ここまでBFS ---


# 白(0)と黒(1)のグループに分ける
group_white = []
group_black = []
for i in range(N):
    if colors[i] == 0:
        group_white.append(i + 1)  # 1-indexedに戻して追加
    else:
        group_black.append(i + 1)

# N/2個以上ある方のグループを出力
if len(group_white) >= N // 2:
    print(*group_white[: N // 2])
else:
    print(*group_black[: N // 2])
