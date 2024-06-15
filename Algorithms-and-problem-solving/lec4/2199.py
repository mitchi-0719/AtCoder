def clamp(n):
    return max(0, min(255, n))


def solve(n, m):
    c = [int(input()) for _ in range(m)]
    x = [0] + [int(input()) for _ in range(n)]

    dp = [[float("inf") for _ in range(256)] for _ in range(n + 1)]
    dp[0][128] = 0

    for i in range(1, n + 1):
        for j in range(256):
            for k in c:
                dp[i][clamp(j + k)] = min(
                    dp[i][clamp(j + k)],
                    dp[i - 1][j] + (clamp(j + k) - x[i]) ** 2,
                )

    print(min(dp[n]))


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()
    solve(n, m)
