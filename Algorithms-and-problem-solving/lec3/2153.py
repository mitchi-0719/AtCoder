def solve(w, h):
    l, r = [], []
    for _ in range(h):
        li, ri = input().split()
        l.append(li)
        r.append(ri[::-1])

    print(l, r)


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit()
    solve(w, h)
