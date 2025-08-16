import collections

N = int(input())
texts = [input() for _ in range(N)]

counter = collections.Counter(texts)

max_count = max(counter.values())
max_texts = []
for k, v in counter.items():
    if v == max_count:
        max_texts.append(k)

max_texts.sort()
for text in max_texts:
    print(text)
