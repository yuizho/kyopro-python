N = int(input())
heights = list(map(int, input().split()))

result = 0
result += heights[0]

for i in range(1, N):
    if heights[i] > heights[i - 1]:
        result += heights[i] - heights[i - 1]

print(result)
