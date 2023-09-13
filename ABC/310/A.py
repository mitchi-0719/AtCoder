n, p, q = map(int, input().split())
d = list(map(int, input().split()))

min_d = min(d)

if min_d + q < p:
    print(min_d + q)
else:
    print(p)