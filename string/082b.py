s = input()
t = input()

sorted_s = "".join(sorted(s))
sorted_t = "".join(sorted(t, reverse=True))

if sorted_s < sorted_t:
    print("Yes")
else:
    print("No")
