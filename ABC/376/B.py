n, q = map(int, input().split())
l, r = 0, 1

ans = 0

for i in range(q):
    c, p = input().split()
    p = int(p) - 1

    if c == "R":
        h = r
        b = l
    else:
        h = l
        b = r

    l_dist = h - p if h - p >= 0 else h - p + n
    r_dist = p - h if p - h >= 0 else p - h + n

    t = True
    for j in range(r_dist):
        if (h + j) % n == b:
            t = False
            break

    if t:
        ans += r_dist
    else:
        ans += l_dist

    if c == "R":
        r = p
    else:
        l = p

print(ans)
