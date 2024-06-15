from collections import defaultdict
import math

memo = defaultdict(int)


def solve(m):
    if memo[m] != 0:
        return memo[m]

    ans = 0
    for i in range(1, int(math.sqrt(m)) + 1):
        if m % i == 0:
            ans += 1 if i * i == m else 2

    memo[m] = ans
    return memo[m]


n = int(input())
cnt = 0
for i in range(1, n):
    cnt += solve(i) * solve(n - i)

print(cnt)
