first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
table = [first, second, third]

b_results = [[], [], []]
for i in range(3):
    for a in range(101):
        for b1 in range(101):
            for b2 in range(101):
                for b3 in range(101):
                    if (
                        table[i][0] == a + b1
                        and table[i][1] == a + b2
                        and table[i][2] == a + b3
                    ):
                        b_results[i].append((b1, b2, b3))

for b1 in b_results[0]:
    if b1 in b_results[1] and b1 in b_results[2]:
        print("Yes")
        exit(0)

print("No")
