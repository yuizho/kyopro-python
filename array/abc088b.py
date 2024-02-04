# https://atcoder.jp/contests/abc088/tasks/abc088_b

N = int(input())
A = list(map(int, input().split()))

sorted_cards = sorted(A, reverse=True)
alice_score = sum([x for i, x in enumerate(sorted_cards) if i % 2 == 0])
bob_score = sum([x for i, x in enumerate(sorted_cards) if i % 2 != 0])

print(alice_score - bob_score)
