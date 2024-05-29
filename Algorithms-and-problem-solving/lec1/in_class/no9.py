def solve(n, r, p, c):
    card = [n - i for i in range(n)]
    for i in range(r):
        m = card[p[i] - 1 : p[i] + c[i] - 1]
        card = m + card[: p[i] - 1] + card[p[i] + c[i] - 1 :]

    print(card[0])


while True:
    n, r = map(int, input().split())
    if n == r == 0:
        exit()

    p, c = [], []
    for i in range(r):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    solve(n, r, p, c)
