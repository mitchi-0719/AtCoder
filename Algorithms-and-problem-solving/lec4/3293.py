def solve(k):
    c = [0] + list(map(int, list(input())))
    n = len(c)
    dp = [[-float("inf") for _ in range(k)] for __ in range(n)]
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(k):
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i - 1][(j - 1) % k] + c[i] * (10 ** (k - ((j - 1) % k) - 1)),
            )

    print(dp[n - 1][0])


while True:
    k = int(input())
    if k == 0:
        exit()
    solve(k)
