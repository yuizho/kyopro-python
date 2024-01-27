# https://atcoder.jp/contests/typical90/tasks/typical90_bo

N, K = map(int, input().split())


def base_n_to_base10(num: int, source_base: int) -> int:
    return int(str(num), source_base)


def base10_to_base_n(num: int, dest_base: int) -> int:
    assert dest_base <= 10, "11進数以上への変換は未対応"
    converted = ""
    while num >= dest_base:
        converted += str(num % dest_base)
        num //= dest_base
    converted += str(num)
    return int(converted[::-1])


def base_n_to_base_m(num: int, source_base: int, dest_base: int) -> int:
    return base10_to_base_n(base_n_to_base10(num, source_base), dest_base)


kokuban = N
for k in range(K):
    replaced = str(base_n_to_base_m(kokuban, 8, 9)).replace("8", "5")
    kokuban = int(replaced)

print(kokuban)
