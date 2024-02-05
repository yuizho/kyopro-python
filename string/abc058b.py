import itertools


O = input()
E = input()

zipped = itertools.zip_longest(list(O), list(E), fillvalue="")

result = ""
for o, e in zipped:
    result = result + o + e

print(result)
