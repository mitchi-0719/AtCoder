def solve(n, m):
    start = 128
    dp = [[0 for _ in range(m)] for __ in range(n)]
    c = []

    for i in range(m):
        ci = int(input())
        c.append(ci)
        dp[0][i] = start + ci
    x = [int(input()) for _ in range(n)]
    print(dp)


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()
    solve(n, m)
