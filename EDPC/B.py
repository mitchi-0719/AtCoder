n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * n
dp[0] = 0

for i in range(1, n):
    m = float("inf")
    for j in range(1, k + 1):
        if i - j >= 0:
            m = min(m, dp[i - j] + abs(h[i] - h[i - j]))
    dp[i] = m

print(dp[-1])
