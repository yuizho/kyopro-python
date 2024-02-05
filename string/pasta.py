import re


S = input()

if re.match(r"^[0-9]{3}$", S):
    print(int(S) * 2)
else:
    print("error")
