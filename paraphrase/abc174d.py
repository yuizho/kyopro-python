N = int(input())
C = input()

R_count = C.count("R")

result = 0
for i in range(R_count):
    if C[i] == "W":
        result += 1

print(result)
