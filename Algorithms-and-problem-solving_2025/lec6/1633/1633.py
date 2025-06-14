def solve():
    h, w = map(int, input().split())
    if h == 0:
        return 1

    r = [input() for _ in range(h)]
    s = input()
    ans = 0

    d = dict()
    for i in range(h):
        for j in range(w):
            d[r[i][j]] = (i, j)

    cur = [0, 0]
    for si in s:
        pos = d[si]
        ans += abs(pos[0] - cur[0]) + abs(pos[1] - cur[1]) + 1
        cur = pos

    print(ans)


while not solve():
    ...
