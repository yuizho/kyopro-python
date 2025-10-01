import collections


N = int(input())

words: collections.defaultdict = collections.defaultdict(int)
max_count = 0
for _ in range(N):
    word = input()
    words[word] += 1
    max_count = max(max_count, words[word])

result = []
for w, c in words.items():
    if max_count == c:
        result.append(w)

for w in sorted(result):
    print(w)
