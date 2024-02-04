# https://atcoder.jp/contests/abc201/tasks/abc201_b

N = int(input())
moutains = []
for n in range(N):
    S, T = input().split()
    moutains.append((S, int(T)))

moutains.sort(key=lambda t: t[1], reverse=True)

print(moutains[1][0])
