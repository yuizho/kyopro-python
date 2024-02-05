# https://atcoder.jp/contests/abc104/tasks/abc104_b

S = input()

if (
    S[0] == "A"
    and S[2:-1].count("C") == 1
    and S.replace("A", "").replace("C", "").islower()
):
    print("AC")
else:
    print("WA")
