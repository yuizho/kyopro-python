N = int(input())

scores_1 = [0] * (N + 1)
scores_2 = [0] * (N + 1)
for i in range(1, N + 1):
    c, p = map(int, input().split())
    scores_1[i] = scores_1[i - 1]
    scores_2[i] = scores_2[i - 1]
    if c == 1:
        scores_1[i] += p
    else:
        scores_2[i] += p

# print(scores_1)
# print(scores_2)

Q = int(input())
for _ in range(Q):
    left, right = map(int, input().split())
    left -= 1
    result1 = scores_1[right] - scores_1[left]
    result2 = scores_2[right] - scores_2[left]
    print(result1, result2)
