def solve(N, n, d):
    p = [[0, 0]]

    for i in range(1, N):
        _p = []
        if d[i - 1] == 0:
            _p = [p[n[i - 1]][0] - 1, p[n[i - 1]][1]]

        elif d[i - 1] == 1:
            _p = [p[n[i - 1]][0], p[n[i - 1]][1] + 1]

        elif d[i - 1] == 2:
            _p = [p[n[i - 1]][0] + 1, p[n[i - 1]][1]]

        else:
            _p = [p[n[i - 1]][0], p[n[i - 1]][1] - 1]
        p.append(_p)

    print(
        abs(max([v[0] for v in p]) - min([v[0] for v in p])) + 1,
        abs(max([v[1] for v in p]) - min([v[1] for v in p])) + 1,
    )


while True:
    N = int(input())
    if N == 0:
        exit()
    n, d = [], []
    for i in range(N - 1):
        ni, di = map(int, input().split())
        n.append(ni)
        d.append(di)

    solve(N, n, d)
