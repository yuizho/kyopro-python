import collections


N, K = map(int, input().split())
balls = list(map(int, input().split()))

ball_counts = sorted(collections.Counter(balls).values())

if len(ball_counts) <= K:
    print(0)
    exit()

diff_count = len(ball_counts) - K
print(sum(ball_counts[:diff_count]))
