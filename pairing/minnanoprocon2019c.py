K, A, B = map(int, input().split())

if A >= B:
    print(1 + K)
    exit()

cookie = 1
money = 0
max_cookie = cookie
for i in range(K):
    if cookie >= A and i < K - 1:
        cookie -= A
        money += 1
        print("exchange cookie to money")
    elif money > 0:
        cookie += B
        money -= 1
        print("exchange money to cookie")
    else:
        cookie += 1
        print("add cookie")
    max_cookie = max(max_cookie, cookie)

print(max_cookie)
