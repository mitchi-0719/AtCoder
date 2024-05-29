# nとmの最大公約数は m と (n/mのあまり)の最大公約数に等しい


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


a, b = map(int, input().split())
print(gcd(a, b))
