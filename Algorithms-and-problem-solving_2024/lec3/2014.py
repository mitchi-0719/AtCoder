def solve(w, h):
    a = []
    for _ in range(h):
        a.append(list(input()))

    print(a)


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit()

    solve(w, h)
