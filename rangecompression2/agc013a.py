N = int(input())
A = list(map(int, input().split()))

result = 0
# ニュートラル: None, 増加: True, 減少: False
increasing = None
for i in range(1, N):
    if increasing is None:
        if A[i - 1] < A[i]:
            increasing = True
        elif A[i - 1] > A[i]:
            increasing = False
    elif increasing and A[i - 1] > A[i]:
        result += 1
        increasing = None
    elif not increasing and A[i - 1] < A[i]:
        result += 1
        increasing = None

print(result + 1)
