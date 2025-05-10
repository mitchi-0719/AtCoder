def solve(s1, s2):
    if s1 == s2:
        print("IDENTICAL")
        return

    prog_s1 = ""
    prog_s2 = ""
    quot1 = [""]
    quot2 = [""]
    q1_idx = 0
    q2_idx = 0

    q = True
    for _s in s1:
        if _s == '"':
            if q:
                quot1.append("")
                prog_s1 += " "
            else:
                q1_idx += 1
            q = not q
        else:
            if q:
                prog_s1 += _s
            else:
                quot1[q1_idx] += _s

    q = True
    for _s in s2:
        if _s == '"':
            if q:
                quot2.append("")
                prog_s2 += " "
            else:
                q2_idx += 1
            q = not q
        else:
            if q:
                prog_s2 += _s
            else:
                quot2[q2_idx] += _s

    if prog_s1 != prog_s2 or len(quot1) != len(quot2):
        print("DIFFERENT")
        return

    diff = 0
    for i in range(len(quot1)):
        diff += 0 if quot1[i] == quot2[i] else 1

    if diff <= 1:
        print("CLOSE")
    else:
        print("DIFFERENT")


while True:
    s1 = input()
    if s1 == ".":
        exit()
    s2 = input()

    solve(s1, s2)
