n, d = map(int, input().split())
t, l = [], []

for _ in range(n):
    ti, li = map(int, input().split())
    t.append(ti)
    l.append(li)

for k in range(1, d + 1):
    m = 0
    for i in range(n):
        m = max(m, t[i] * (l[i] + k))
    print(m)
