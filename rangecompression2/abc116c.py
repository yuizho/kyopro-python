N = int(input())
H = list(map(int, input().split()))

garden = [0] * N

result = 0
while H != garden:
    streak = False
    for i in range(N):
        if H[i] - garden[i] > 0:
            garden[i] += 1
            if not streak:
                result += 1
            streak = True
        else:
            streak = False
        # print(garden)

print(result)
