N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for i in range(N):
    diff += abs(B[i] - A[i])

if diff > K:
    print("No")
    exit()

is_k_even = K % 2 == 0
is_diff_even = diff % 2 == 0
if is_k_even == is_diff_even:
    print("Yes")
else:
    print("No")
