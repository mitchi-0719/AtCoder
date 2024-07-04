n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for bi in b:
    ai = a[bi]
    a[bi] = 0
    for i in range(min(n, ai)):
        add = ai // n + (1 if ai % n > i else 0)
        a[(bi + 1 + i) % n] += add

print(*a)
