N = int(input())
S = input()

alphabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2

result = ""
for s in S:
    index = alphabe.find(s)
    result += alphabe[index + N]

print(result)
