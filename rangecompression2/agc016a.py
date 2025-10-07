S = input()
N = len(S)

# Sに含まれるユニークな文字を取得する
# 例: "abacaba" -> {'a', 'b', 'c'}
unique_chars = set(S)

# 答えを格納する変数。最初は十分大きい値（文字列長）で初期化。
min_operations = N

# 各ユニーク文字をターゲットにしてループ
for target_char in unique_chars:
    # target_charに揃えるための最小ターン数を計算
    # これは「target_char以外の文字の最大連続長」に等しい
    max_gap = 0
    current_gap = 0

    # 文字列を最初から最後までスキャン
    for char in S:
        if char == target_char:
            # ターゲット文字が来たら、それまでのギャップを確定し、リセット
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            # ターゲット文字でなければ、ギャップを1増やす
            current_gap += 1

    # ループ終了後、最後のギャップを考慮に入れる
    # 例: S = "abct" で target = 'a' の場合、ループ後の "bct" (gap=3) を反映させる
    max_gap = max(max_gap, current_gap)

    # 全ターゲット文字の結果のうち、最小のものを探す
    min_operations = min(min_operations, max_gap)

print(min_operations)
