def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    pmx = [0 for _ in range(n)]
    pmn = [0 for _ in range(n)]
    for _ in range(m):
        [s, k, *c] = list(map(int, input().split()))
        if k == 1:
            pmn[c[0] - 1] += s
        for ci in c:
            pmx[ci - 1] += s

    mi, mv = max(enumerate(pmx), key=lambda x: x[1])
    lv = min(pmn[i] for i in range(n) if i != mi)

    print(mv - lv + 1)


while 1:
    if solve():
        break
