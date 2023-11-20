n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(1, n):
    m = 10**10
    for j in range(i - 1, i - k - 1, -1):
        if j < 0:
            break
        m = min(m, dp[j] + abs(h[i] - h[j]))
    dp[i] = m

print(dp[-1])
