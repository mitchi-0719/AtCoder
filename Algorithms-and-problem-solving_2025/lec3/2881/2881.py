def solve():
    s = input()
    if s == "#":
        return True

    _, y, m, d = s.split()
    y, m, d = map(int, [y, m, d])

    if y <= 30:
        print(s)
    elif 32 <= y:
        print("?", y - 30, m, d)
    else:
        if m <= 4:
            print(s)
        else:
            print("?", y - 30, m, d)


while 1:
    if solve():
        break
