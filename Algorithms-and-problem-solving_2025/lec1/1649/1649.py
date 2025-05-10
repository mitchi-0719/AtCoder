def solve():
    w, h = map(int, input().split())
    if w == h == 0:
        return True

    k = w + h - 1
    xy = []
    for _ in range(k):
        x, y, _ = map(int, input().split())
        xy.append([x - 1, y - 1])

    u = [False for _ in range(w)]
    l = [False for _ in range(h)]
    u[0] = True

    for _ in range(k):
        for i in range(k):
            x, y = xy[i]
            if u[x] or l[y]:
                u[x] = l[y] = True

    if u + l == [True for _ in range(len(u + l))]:
        print("YES")
    else:
        print("NO")


while 1:
    if solve():
        break
