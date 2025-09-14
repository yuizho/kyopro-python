from typing import Counter

N = int(input())
A = list(map(int, input().split()))

# 1. カードの種類数を数える
count_by_num = Counter(A)
c = len(count_by_num)

# 2. 重複カードの枚数を計算する
d = N - c

# 3. 重複カードの枚数が偶数か奇数かで判断する
if d % 2 == 0:
    # 偶数なら、種類数 c がそのまま答え
    print(c)
else:
    # 奇数なら、種類数が1つ減る
    print(c - 1)
