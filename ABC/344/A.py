p = True
for si in input():
    if p and si != "|":
        print(si, end="")
    elif si == "|":
        p = not p
print()
