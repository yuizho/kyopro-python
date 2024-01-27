# https://atcoder.jp/contests/abc165/tasks/abc165_b


X = int(input())

year = 0
yokin = 100
while yokin < X:
    year += 1
    yokin += yokin // 100

print(year)
