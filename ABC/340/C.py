from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

memo = defaultdict(int)


def solve(n):
    if n == 1:
        return 0

    if memo[n] == 0:
        memo[n] = n + solve(n // 2 + n % 2) + solve(n // 2)

    return memo[n]


print(solve(int(input())))
