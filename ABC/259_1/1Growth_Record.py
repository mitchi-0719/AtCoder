#AC

n, m, x, t, d = map(int, input().split())

if m >= x:
    print(t)
else:
    while x > m:
        t -= d
        x -= 1
    print(t)