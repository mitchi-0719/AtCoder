def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    p = [list(map(int, input().split())) for _ in range(m)]
    ans = 0

    for k in range(n):
        s = 0
        for j in range(m):
            s += p[j][k]

        ans = max(ans, s)

    print(ans)


while 1:
    if solve():
        break
