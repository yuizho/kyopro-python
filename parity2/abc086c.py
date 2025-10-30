N = int(input())

current_t = 0
current_x = 0
current_y = 0
result = "Yes"
for _ in range(N):
    t, x, y = map(int, input().split())

    diff_t = t - current_t
    diff_x = abs(x - current_x)
    diff_y = abs(y - current_y)
    is_time_even = diff_t % 2 == 0
    is_distance_even = (diff_x + diff_y) % 2 == 0

    if diff_t < (diff_x + diff_y) or is_time_even != is_distance_even:
        result = "No"

    current_t = t
    current_x = x
    current_y = y

print(result)
