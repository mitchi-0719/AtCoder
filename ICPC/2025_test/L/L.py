def solve():
    s1 = input()
    if s1 == "#":
        return 1

    s2 = input()
    print("Yes" if s1 < s2 else "No")


while not solve():
    ...
