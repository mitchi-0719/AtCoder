# nとmの最小公倍数は n*m // nとnの最大公約数で求められる。


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def lcm(n, m):
    return (n * m) // gcd(n, m)


a, b = map(int, input().split())
print(lcm(a, b))
