def calc(s):
    buf = ""
    ans = 0
    for si in s:
        if len(buf) == 3:
            ans += int(buf)
            buf = ""

        buf += si

    ans += int(buf)
    return ans


def solve():
    k = int(input())
    if k == 0:
        return 1

    s = "0" + input()
    l = len(s)
    dp = [[-1] * k for _ in range(l)]
    dp[0][0] = 0

    for i in range(1, l):
        for j in range(k):
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i - 1][(j - 1) % k] + int(s[i]) * (10 ** (k - ((j - 1) % k) - 1)),
            )

    print(dp[l - 1][0])


while not solve():
    ...
