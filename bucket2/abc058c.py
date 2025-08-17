from collections import Counter, defaultdict


n = int(input())
texts = [Counter(input()) for _ in range(n)]


result = dict(texts[0])
for i in range(1, len(texts)):
    temp = dict(result)
    for c, count in result.items():
        if c in texts[i]:
            if texts[i][c] < count:
                temp[c] = texts[i][c]
                continue
        else:
            del temp[c]
    result = temp

result_str = ""
for c, count in result.items():
    result_str += c * count

print("".join(sorted(result_str)))
