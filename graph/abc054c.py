N, M = map(int, input().split())

graph: list[list[int]] = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(current_v, visited):
    # 現在の頂点を訪問済みリストに追加
    visited.append(current_v)

    # すべての頂点を訪問したかチェック
    if len(visited) == N:
        # すべて訪問済みなら、有効なパスが1つ見つかった
        return 1

    # パスの数をカウントする変数
    path_count = 0

    # 現在の頂点から行ける次の頂点をループ
    for next_v in graph[current_v]:
        # 次の頂点がまだ訪問済みでなければ
        if next_v not in visited:
            # 再帰的に次の頂点を探索し、見つかったパスの数を加算
            # visited.copy()でリストのコピーを渡すのが重要！
            path_count += dfs(next_v, visited.copy())

    return path_count


# 頂点0（問題の頂点1）から探索を開始
# 最初のvisitedリストは空でOK
ans = dfs(0, [])

print(ans)
