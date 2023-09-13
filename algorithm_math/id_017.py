n = int(input())
a = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def lcm(n, m):
    return n*m // gcd(n, m)

l = lcm(a[0], a[1])
for i in range(2, n):
    l = lcm(a[i], l)

print(l)