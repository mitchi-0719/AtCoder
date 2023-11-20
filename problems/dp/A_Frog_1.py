n = int(input())
h = list(map(int, input().split()))
inf = 10**10

dp = [inf for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = min(dp[1], abs(h[1] - h[0]))
    else:
        dp[i] = min(
            dp[i], dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2])
        )

print(dp[-1])
