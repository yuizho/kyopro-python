N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

result = 1
trend = 0
for i in range(1, N):
    current_trend = nums[i] - nums[i - 1]

    if current_trend == 0:
        continue

    # print(f"{trend=}, {current_trend=}")
    if (current_trend < 0 and trend > 0) or (current_trend > 0 and trend < 0):
        result += 1
        # トレンドが切り替わったら一旦リセット
        trend = 0
    else:
        trend = current_trend

print(result)
