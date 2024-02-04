# https://atcoder.jp/contests/abc121/tasks/abc121_c

N, M = map(int, input().split())
stores = []
for _ in range(N):
    price, stock = map(int, input().split())
    stores.append((price, stock))

stores.sort(key=lambda x: x[0])

needs = M
spent = 0
for store in stores:
    count = min(needs, store[1])
    spent += count * store[0]
    needs -= count
    if needs == 0:
        break

print(spent)
