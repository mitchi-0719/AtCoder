s = input()
box = set()
tmp = [[]]
tmp_i = 0

for i, si in enumerate(s):
    if si == "(":
        if len(tmp) >= tmp_i:
            tmp.append([])
        tmp_i += 1
    elif si == ")":
        for ti in tmp[tmp_i]:
            box.discard(ti)
        tmp[tmp_i].clear()
        tmp_i -= 1
    else:
        if si not in box:
            tmp[tmp_i].append(si)
            box.add(si)
        else:
            print("No")
            exit()

print("Yes")
