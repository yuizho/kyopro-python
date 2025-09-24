N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
# 5重ループで5つの異なる数を選ぶ
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    # 掛け算のたびに % P を行い、数を小さく保つ
                    # A[i]は元々P未満なので、最初の剰余は省略できる
                    product = A[i]
                    product = (product * A[j]) % P
                    product = (product * A[k]) % P
                    product = (product * A[l]) % P
                    product = (product * A[m]) % P

                    if product == Q:
                        ans += 1
print(ans)
