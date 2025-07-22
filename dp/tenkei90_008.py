N = input()
S = input()

MOD = 1_000_000_007

target = "atcoder"
target_len = len(target)

dp = [0] * (target_len + 1)
dp[0] = 1

for s in S:
    for i in range(target_len):
        if s == target[i]:
            # dp[i + 1]はsのパターン個数を入れていくdp
            # dp[0]は1になっているのとdp[1:]は0で初期化されているので、
            # dp[i + 1] + dp[i]を足し合わせることでパターンが出せる
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD

print(dp[target_len])
