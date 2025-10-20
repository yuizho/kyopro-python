import math

# math.gcd が最大公約数を計算してくれます
# Python 3.8未満では fractions.gcd を使います

N = int(input())
A = list(map(int, input().split()))

# N=2 の場合は特別
if N == 2:
    print(max(A[0], A[1]))
    exit()

# L[i]: A[0]...A[i] のGCD
# (0-indexedで実装します)
L = [0] * N
L[0] = A[0]
for i in range(1, N):
    L[i] = math.gcd(L[i - 1], A[i])

# R[i]: A[i]...A[N-1] のGCD
R = [0] * N
R[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    R[i] = math.gcd(A[i], R[i + 1])

ans = 0

# i=0 (先頭) を書き換える場合
# A[1]...A[N-1] のGCDは R[1]
ans = max(ans, R[1])

# i=N-1 (末尾) を書き換える場合
# A[0]...A[N-2] のGCDは L[N-2]
ans = max(ans, L[N - 2])

# i=1...N-2 (中間) を書き換える場合
for i in range(1, N - 1):
    # A[0]...A[i-1] と A[i+1]...A[N-1] のGCD
    current_gcd = math.gcd(L[i - 1], R[i + 1])
    ans = max(ans, current_gcd)

print(ans)
