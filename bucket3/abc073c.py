N = int(input())

paper: set[int] = set()
for _ in range(N):
    num = int(input())

    if num in paper:
        paper.remove(num)
    else:
        paper.add(num)

print(len(paper))
