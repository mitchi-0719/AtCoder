import pprint

n = int(input())
sunuke = []

for _ in range(n):
    sunuke.append(list(map(int, input().split())))

dp = [[-1 for _ in range(5)] for __ in range(n + 1)]

dp[0][0] = 0
before = 0
for i in range(1, n + 1):
    [t, x, a] = sunuke[i - 1]
    for j in range(5):
        if dp[i - 1][j] != -1:
            for k in range(5):
                if abs(j - k) <= abs(t - before):
                    dp[i][k] = max(dp[i][k], dp[i - 1][j] + (a if x == k else 0))
    before = t

print(max(dp[-1]))
