# https://atcoder.jp/contests/abc113/tasks/abc113_c

from operator import itemgetter


N, M = map(int, input().split())

shis = []
for m in range(M):
    ken, year = map(int, input().split())
    shis.append({"ken": ken, "year": year, "src_order": m})

shis.sort(key=itemgetter("ken", "year"))

current_ken = 0
shi_index = 0
ids = []
for shi in shis:
    if current_ken != shi["ken"]:
        current_ken = shi["ken"]
        shi_index = 1
    else:
        shi_index += 1
    ids.append((f"{current_ken:06}{shi_index:06}", shi["src_order"]))

result = map(lambda x: x[0], sorted(ids, key=lambda x: x[1]))
print(*result, sep="\n")
