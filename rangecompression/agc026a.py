N = int(input())
slimes = list(map(int, input().split()))

result = 0
i = 0
while i < N - 1:
    j = i + 1
    same_count = 1
    while j < N and slimes[j] == slimes[i]:
        same_count += 1
        j += 1

    result += same_count // 2

    i = j

print(result)
