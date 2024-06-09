# nとmの最大公約数は m と (n/mのあまり)の最大公約数に等しい
from collections import defaultdict

memo = defaultdict(lambda: float("inf"))


def gcd(n, m):
    if m == 0:
        return n
    else:
        if memo[(n, m)] != float("inf"):
            return memo[(n, m)]

        memo[(n, m)] = gcd(m, n % m)
        return memo[(n, m)]


a, b = map(int, input().split())
print(gcd(a, b))
