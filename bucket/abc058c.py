from collections import Counter


N = int(input())
mojis = [input() for _ in range(N)]

moji_counters = []
for moji in mojis:
    moji_counters.append(Counter(moji))

result_moji_counter = moji_counters[0]
for moji_counter in moji_counters[1:]:
    result_moji_counter = result_moji_counter & moji_counter

for k in sorted(result_moji_counter):
    if result_moji_counter[k] > 0:
        print(k * result_moji_counter[k], end="")

print()
