n = int(input())

dp = [0] * n

for i in range(n):
    a = list(map(int, input().split()))
    if i == 0:
        dp[0] = max(a)
        select = a.index(max(a))
    else:
        dp[i] = dp[i - 1] + max([a[j] for j in range(3) if j != select])
        select = a.index(max([a[j] for j in range(3) if j != select]))

print(dp[-1])
