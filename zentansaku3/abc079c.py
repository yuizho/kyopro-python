import itertools


A, B, C, D = map(int, input())
# ops = ["---", "+--", "-+-", "--+", "++-", "+-+", "-++", "+++"]
ops = itertools.product("+-", repeat=3)

for op in ops:
    calculated = A - B if op[0] == "-" else A + B
    calculated = calculated - C if op[1] == "-" else calculated + C
    calculated = calculated - D if op[2] == "-" else calculated + D

    if calculated == 7:
        print(f"{A}{op[0]}{B}{op[1]}{C}{op[2]}{D}=7")
        break
