X, K, D = map(int, input().split())

# サイクルに入るまでのしっぽの回数
n = abs(X) // D

remaining_count = K - n
if remaining_count < 0:
    print(abs(X) - K * D)
    exit()

current_position = abs(X) - D * n
if remaining_count % 2 == 0:
    print(current_position)
else:
    print(abs(current_position - D))
