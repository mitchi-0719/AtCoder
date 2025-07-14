# nとmの最小公倍数は n*m // nとnの最大公約数で求められる。
from functools import lru_cache


@lru_cache(maxsize=None)
def gcd(n, m):
    return n if m == 0 else gcd(m, n % m)


def lcm(n, m):
    return (n * m) // gcd(n, m)


a, b = map(int, input().split())
print(lcm(a, b))
