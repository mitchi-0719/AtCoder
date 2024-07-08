a = []

for _ in range(9):
    ai = list(map(int, input().split()))
    if len(set(ai)) != 9:
        print("No")
        exit()
    a.append(ai)

ret_a = [list(a)[::-1] for a in zip(*a)]

for ai in ret_a:
    if len(set(ai)) != 9:
        print("No")
        exit()

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        tmp = []
        for k in range(3):
            for l in range(3):
                tmp.append(a[i + k][j + l])
        if len(set(tmp)) != 9:
            print("No")
            exit()


print("Yes")
