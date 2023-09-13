s = input()
n = len(s)


if (s.index("B") + (n-s[::-1].index("B"))) % 2 == 0:
    if s.index("R") < s.index("K") < n-s[::-1].index("R"):
        print("Yes")
        exit()

print("No")