N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [x - 1 for x in A]

visited = [-1] * N
path = []

current_town = 0
step = 0

while visited[current_town] == -1:
    visited[current_town] = step
    path.append(current_town + 1)
    current_town = A[current_town]
    step += 1

print(visited)
print(path)
print(f"{current_town=}, {step=}")

tail_len = visited[current_town]
loop_len = step - tail_len

print(f"{tail_len=}, {loop_len=}")

if K < tail_len:
    print(path[K])
else:
    remaining_K = K - tail_len
    loop_index = remaining_K % loop_len

    loop_path = path[tail_len:]
    print(f"{remaining_K=}, {loop_index=}, {loop_path=}")

    print(loop_path[loop_index])
