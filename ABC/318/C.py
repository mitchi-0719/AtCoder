n, d, p = map(int, input().split())
f = list(map(int, input().split()))
sort_f = sorted(f, reverse=True)

di = 0
fin = False
while True:
    s = 0
    for i in range(d):
        if di * d + i >= n:
            fin = True
            di += 1 if s >= p else 0
            break
        s += sort_f[di * d + i]

    if s < p or fin:
        break
    else:
        di += 1

ans = di * p
for i in range(n):
    if di * d <= i:
        ans += sort_f[i]

print(ans)
