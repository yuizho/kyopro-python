# https://atcoder.jp/contests/abc095/tasks/abc095_b

import itertools


N, X = map(int, input().split())
recipes = []
for n in range(N):
    recipes.append(int(input()))

powder = X
powder -= sum(recipes)

min_recipe = min(recipes)
result = N
for _ in itertools.count():
    powder -= min_recipe
    if powder < 0:
        break
    result += 1

print(result)
