N = int(input())
S = [input() for _ in range(N)]

count = 0
A = 0
B = 0
AB = 0

for s in S:
    # 文字列内部の "AB" を数える
    count += sum(1 for i in range(len(s) - 1) if s[i : i + 2] == "AB")

    if s.startswith("B") and s.endswith("A"):
        AB += 1
    elif s.startswith("B"):
        B += 1
    elif s.endswith("A"):
        A += 1

if A == 0 and B == 0:
    print(count + max(AB - 1, 0))
else:
    print(count + AB + min(A, B))
