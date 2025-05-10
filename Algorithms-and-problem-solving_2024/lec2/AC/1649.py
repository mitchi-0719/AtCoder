def solve(w, h):
    t = [False for i in range(w)]
    l = [False for _ in range(h)]
    p = []
    t[0] = True

    for k in range(w + h - 1):
        x, y, n = map(int, input().split())
        p.append([x - 1, y - 1])

    for _ in range(w + h - 1):
        for k in range(h + w - 1):
            x, y = p[k]
            if t[x] or l[y]:
                t[x] = l[y] = True

    print("YES" if len(set(l + t)) == 1 and list(set(l + t))[0] else "NO")


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit()
    solve(w, h)
