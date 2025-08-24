S = input()
K = int(input())

if len(set(S)) == 1:
    ans = (len(S) * K) // 2
    print(ans)
    exit()


def count_changes(text):
    L = list(text)
    for i in range(1, len(text)):
        if L[i - 1] == L[i]:
            L[i] = "_"
            # print(L)
    return L.count("_")


changes_S = count_changes(S)
changes_S2 = count_changes(S + S)

diff = changes_S2 - changes_S

print(changes_S + diff * (K - 1))
