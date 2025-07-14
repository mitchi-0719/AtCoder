from functools import lru_cache


@lru_cache(maxsize=None)
def gcd(n, m):
    return n if m == 0 else gcd(m, n % m)


a, b = map(int, input().split())
print(gcd(a, b))
