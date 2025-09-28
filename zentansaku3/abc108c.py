N, K = map(int, input().split())

# 各余りの個数を数える
counts = [0] * K
for i in range(1, N + 1):
    counts[i % K] += 1

print(counts)

ans = 0
for a in range(K):
    b = (K - a) % K
    c = (K - a) % K
    if (b + c) % K != 0:
        continue
    ans += counts[a] * counts[b] * counts[c]
    print(f"{counts[a]=}, {counts[b]=}, {counts[c]=}")

print(ans)
