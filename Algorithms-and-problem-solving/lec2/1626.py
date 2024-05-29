def solve(l, h):
    i = l
    ans = h
    while l < h:
        m = (h + l) // 2
        sn = (i * m) + ((m**2) / 2) - (m / 2)
        if sn == ans:
            return m
        elif sn < ans:
            l = m - 1
        else:
            h = m + 1
        print(l, h)
    return -1


while True:
    b = int(input())
    if b == 0:
        exit()

    for i in range(1, b):
        ans = solve(i, b)
        if ans != -1:
            print(i, ans)
            break
