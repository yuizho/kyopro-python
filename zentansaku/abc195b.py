A, B, W = map(int, input().split())
W = W * 1000

results = []
for i in range(1, 10**6 + 1):
    if A <= W / i <= B:
        results.append(i)

if results:
    print(min(results), max(results))
    exit()
print("UNSATISFIABLE")
