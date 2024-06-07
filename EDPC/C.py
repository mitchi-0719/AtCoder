n = int(input())

dp = [[-1 for _ in range(n)] for __ in range(3)]

x = [list(map(int, input().split())) for _ in range(n)]

dp[0][0] = dp[1][0] = dp[2][0] = 0

print(dp)
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + x[i][j])
print(dp)
print(max([dp[n - 1][i] for i in range(3)]))
