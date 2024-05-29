while True:
    t, d, l = map(int, input().split())
    if t == d == l == 0:
        exit()

    w = 0
    ans = 0

    for _ in range(t):
        x = int(input())
        if x >= l:
            w = d
        if w > 0:
            ans += 1
        w -= 1
    print(ans - 1 if ans != 0 else 0)
