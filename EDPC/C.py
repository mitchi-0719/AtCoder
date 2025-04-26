n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for __ in range(n + 1)]


for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + abc[i][j])

print(max(dp[-1]))
