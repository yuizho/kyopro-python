N = int(input())
nums = [int(input()) for _ in range(N)]

paper: dict[int, int] = {}
for n in nums:
    if n in paper:
        del paper[n]
        continue

    paper[n] = 1

print(len(paper))
