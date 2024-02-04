# https://atcoder.jp/contests/abc132/tasks/abc132_c


N = int(input())
difficulties = list(map(int, input().split()))

difficulties.sort()
mid_index = len(difficulties) // 2

print(difficulties[mid_index] - difficulties[mid_index - 1])
