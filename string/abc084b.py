import re


A, B = map(int, input().split())
S = input()


if re.match(rf"^[0-9]{{{A}}}-[0-9]{{{B}}}$", S):
    print("Yes")
else:
    print("No")
