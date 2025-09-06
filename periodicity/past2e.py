N = int(input())
to = [0] + list(map(int, input().split()))  # 1-indexed
ans = [0] * (N + 1)
seen = [False] * (N + 1)

for s in range(1, N + 1):
    if ans[s]:  # 既にサイクル長が確定
        continue
    if seen[s]:  # 既に他の開始点で辿っている（順列なのでここはほぼ不要）
        continue

    cur = s
    cycle = []
    while True:
        seen[cur] = True
        cycle.append(cur)
        cur = to[cur]
        if cur == s:  # s に戻った＝サイクル1周
            break

    L = len(cycle)
    for v in cycle:
        ans[v] = L

print(*ans[1:])
