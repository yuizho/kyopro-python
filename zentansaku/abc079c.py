import itertools


A, B, C, D = map(int, input())

operations = itertools.product("+-", repeat=3)


def to_operation(o):
    if o == "+":
        return lambda x, y: x + y
    else:
        return lambda x, y: x - y


for o in operations:
    op1 = to_operation(o[0])(A, B)
    op2 = to_operation(o[1])(op1, C)
    op3 = to_operation(o[2])(op2, D)
    if op3 == 7:
        print(f"{A}{o[0]}{B}{o[1]}{C}{o[2]}{D}=7")
        exit(0)
