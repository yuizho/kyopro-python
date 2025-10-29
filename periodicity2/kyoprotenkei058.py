# 各桁の和を計算するヘルパー関数
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


N, K = map(int, input().split())

# visited[i] = k は、数字iにkステップ目に到達したことを示す
# 未到達は-1で初期化
visited = [-1] * 100000
# 実際に通った経路(数字)を記録するリスト
path = []

X = N
step = 0

# ステップ1: ループを検出するまでシミュレーション
while visited[X] == -1:
    visited[X] = step
    path.append(X)

    X = (X + sum_digits(X)) % 100000
    step += 1

# ステップ2: しっぽとループの長さを計算
# X はループの開始地点
# step は ループ開始地点に2回目に来たステップ数
# visited[X] は ループ開始地点に1回目に来たステップ数
tail_len = visited[X]
loop_len = step - tail_len

# ステップ3: Kステップ後の位置を計算
if K < tail_len:
    # 場合1: Kがしっぽの長さより短い
    print(path[K])
else:
    # 場合2: Kがループに到達する
    remaining_K = K - tail_len
    loop_index = remaining_K % loop_len

    print(path[tail_len + loop_index])
