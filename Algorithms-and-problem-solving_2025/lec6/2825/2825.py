def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return 1

    p_mx = [0 for _ in range(n)]
    p_mn = [0 for _ in range(n)]

    for _ in range(m):
        s, k, *c = map(int, input().split())
        if k == 1:
            p_mn[c[0] - 1] += s
        for ci in c:
            p_mx[ci - 1] += s

    ans = 0
    mx = max(p_mx)
    mxi = p_mx.index(mx)
    for i in range(n):
        if mxi == i:
            continue
        ans = max(ans, mx - p_mn[i])

    print(ans + 1)


while not solve():
    ...
