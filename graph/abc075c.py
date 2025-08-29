import sys

# 再帰の上限を解放（DFSで必要になることがある）
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# M本の辺をリストに格納しておく
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

# 橋の数をカウントする変数
bridge_count = 0

# 0からM-1番目までの辺を1本ずつ試す
for i in range(M):
    # i番目の辺を「無視」して、残りのM-1本でグラフを構築
    graph: list[list[int]] = [[] for _ in range(N)]
    for j in range(M):
        if i == j:
            # i番目の辺は無視する
            continue

        a, b = edges[j]
        graph[a].append(b)
        graph[b].append(a)

    # --- グラフが連結かどうかを調べる ---
    # visited配列で訪問済みかを管理
    visited = [False] * N

    # DFS関数
    def dfs(v):
        visited[v] = True
        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(next_v)

    # 頂点0からDFSを開始
    dfs(0)

    # 連結判定
    # もしvisitedに一つでもFalseがあれば、0からたどり着けない頂点がある
    # つまりグラフは非連結
    if False in visited:
        # i番目の辺は「橋」だった
        bridge_count += 1

print(bridge_count)
