n = int(input())
a = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

r = gcd(a[0], a[1])
for i in range(2, n):
    r = gcd(a[i], r)

print(r)