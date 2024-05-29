while True:
    n, l, r = map(int, input().split())
    if n == l == r == 0:
        exit()

    a = [int(input()) for _ in range(n)]
    ans = 0
    for x in range(l, r + 1):
        find = False
        for i, ai in enumerate(a):
            if x % ai == 0:
                find = True
                ans += 1 if (i + 1) % 2 == 1 else 0
                break
        if (not find) and n % 2 == 0:
            ans += 1

    print(ans)
