def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    dp = sorted(
        [list(map(int, input().split())) for _ in range(n)],
        reverse=True,
        key=lambda x: x[1],
    )

    ans = 0
    for i in range(n):
        d, p = dp[i]
        if m == 0:
            ans += d * p
        else:
            ans += p * max(0, d - m)
            m = max(0, m - d)

    print(ans)


while 1:
    if solve():
        break
