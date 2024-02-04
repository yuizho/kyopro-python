#  https://atcoder.jp/contests/abc067/tasks/abc067_b

N, K = map(int, input().split())
sticks = list(map(int, input().split()))

result = sum(sorted(sticks, reverse=True)[:K])
print(result)
