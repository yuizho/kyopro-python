N, K = map(int, input().split())


def sum_digits(n):
    s = 0
    # nが0になるまで各桁の和を計算
    while n > 0:
        s += n % 10
        n //= 10
    return s


# visited[i] は、数字iに何ステップ目に到達したかを記録する
visited = [-1] * 100000
# pathは、実際に通った数字の履歴
path = []

X = N
step = 0

# サイクルを検出するまでループ
while visited[X] == -1:
    visited[X] = step
    path.append(X)

    # 次の数字を計算
    X = (X + sum_digits(X)) % 100000
    step += 1

# この時点で、Xはすでに出現済みの数字

# しっぽの長さを計算
tail_len = visited[X]
# ループの長さを計算
loop_len = step - tail_len

if K < tail_len:
    # Kがしっぽの範囲内なら、履歴から直接答えを取り出す
    print(path[K])
else:
    # Kがループの範囲内なら、余りを使って答えを計算
    remaining_K = K - tail_len
    loop_index = remaining_K % loop_len

    # ループ部分のパスはpath[tail_len:]
    print(path[tail_len + loop_index])
