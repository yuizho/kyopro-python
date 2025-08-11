N, P, Q = map(int, input().split())
nums = list(map(int, input().split()))

# numberから5つ選ぶ % P == Q
result = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            for d in range(c + 1, N):
                for e in range(d + 1, N):
                    num = nums[a]
                    num = (num * nums[b]) % P
                    num = (num * nums[c]) % P
                    num = (num * nums[d]) % P
                    num = (num * nums[e]) % P

                    if num == Q:
                        result += 1

print(result)
