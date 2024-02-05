P = map(int, input().split())

result = ""
for p in P:
    result += chr(64 + p)

print(result.lower())
