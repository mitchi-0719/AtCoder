def solve():
    s = input()
    if s == "#":
        return 1

    alf_s = []
    alf_l = []
    num = []

    for si in s:
        if "a" <= si <= "z":
            alf_s.append(si)
        elif "A" <= si <= "Z":
            alf_l.append(si)
        else:
            num.append(si)

    print("".join([*sorted(alf_s), *sorted(alf_l), *sorted(num)]))


while not solve():
    ...
