n, c1, c2 = input().split()
s = input()

for si in s:
    if si == c1:
        print(c1, end="")
    else:
        print(c2, end="")
