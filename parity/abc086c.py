N = int(input())
moves = [list(map(int, input().split())) for _ in range(N)]

prev_time = 0
prev_x = 0
prev_y = 0
result = "Yes"
for m in moves:
    t, x, y = m
    consumed_time = t - prev_time
    distance = abs(x - prev_x) + abs(y - prev_y)
    if consumed_time < distance:
        result = "No"
        break

    if (consumed_time % 2 == 0 and distance % 2 != 0) or (
        consumed_time % 2 != 0 and distance % 2 == 0
    ):
        result = "No"
        break

    prev_x = x
    prev_y = y
    prev_time = t

print(result)
