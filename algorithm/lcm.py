# nとmの最小公倍数は n*m // nとnの最大公約数で求められる。
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


def lcm(n, m):
    return (n * m) // gcd(n, m)


a, b = map(int, input().split())
print(lcm(a, b))
