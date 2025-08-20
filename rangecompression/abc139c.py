N = int(input())
masus = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

i = 0
result = 0
while i < N:
    j = i
    count = 0
    while j < N - 1 and masus[j] >= masus[j + 1]:
        j += 1
        count += 1

    result = max(result, count)

    i = j + 1

print(result)
