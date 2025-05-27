r = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}


def solve():
    s = input()
    if s == "#":
        return 1

    c = 0
    is_r = s[0] in r

    for si in s[1:]:
        if si in r and not is_r:
            is_r = True
            c += 1
        elif si not in r and is_r:
            is_r = False
            c += 1

    print(c)


while 1:
    if solve():
        break
