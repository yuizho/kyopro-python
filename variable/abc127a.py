# https://atcoder.jp/contests/abc127/tasks/abc127_a

age, amount = map(int, input().split())

if age >= 13:
    print(amount)
elif age >= 6 and age <= 12:
    print(amount // 2)
else :
    print(0)