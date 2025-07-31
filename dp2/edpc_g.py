import sys

# ★★★★★ 修正点1：再帰の上限を大きな値に設定 ★★★★★
# Nが最大10^5なので、それより大きい10^6などに設定すると安全
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]


# グラフを隣接リスト形式で表現する
# graph[i] = 頂点i+1から行ける頂点のリスト
graph: list[list[int]] = [[] for _ in range(N)]
for x, y in edges:
    # 0-indexedに調整
    graph[x - 1].append(y - 1)

# dp[i] := 頂点iから始まる最長経路の長さ
# -1は未計算であること
dp = [-1] * N


def dfs(v):
    if dp[v] != -1:
        return dp[v]

    max_len = 0
    for next_v in graph[v]:
        max_len = max(max_len, dfs(next_v) + 1)

    dp[v] = max_len
    return max_len


for i in range(N):
    if dp[i] == -1:
        dfs(i)

print(max(dp))
