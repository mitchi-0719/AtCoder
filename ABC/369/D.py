n = int(input())
a = list(map(int, input().split()))

dp = [[(0, 0) for _ in range(2)] for __ in range(n + 1)]

for i in range(1, n + 1):
    ai = a[i - 1]

    new_value0 = dp[i - 1][0][0] + ai * (2 if dp[i - 1][0][1] % 2 == 1 else 1)
    new_value1 = dp[i - 1][1][0] + ai * (2 if dp[i - 1][1][1] % 2 == 1 else 1)

    if new_value0 > new_value1:
        dp[i][0] = (new_value0, dp[i - 1][0][1] + 1)
    else:
        dp[i][0] = (new_value1, dp[i - 1][1][1] + 1)

    if dp[i - 1][0][0] > dp[i - 1][1][0]:
        dp[i][1] = dp[i - 1][0]
    else:
        dp[i][1] = dp[i - 1][1]

# print(dp)
print(max(dp[-1][0][0], dp[-1][1][0]))
