A, B, C, D = map(int, list(input()))


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


op_pattern = [
    (add, add, add),
    (add, add, minus),
    (add, minus, minus),
    (add, minus, add),
    (minus, add, add),
    (minus, add, minus),
    (minus, minus, add),
    (minus, minus, minus),
]

for op in op_pattern:
    op1 = op[0](A, B)
    op2 = op[1](op1, C)
    op3 = op[2](op2, D)

    op1_str = "+" if op[0] == add else "-"
    op2_str = "+" if op[1] == add else "-"
    op3_str = "+" if op[2] == add else "-"

    if op3 == 7:
        print(f"{A}{op1_str}{B}{op2_str}{C}{op3_str}{D}=7")
        exit()

print("error")
