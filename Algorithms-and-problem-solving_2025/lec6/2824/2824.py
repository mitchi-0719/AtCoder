def solve():
    t, d, l = map(int, input().split())
    if t == d == l == 0:
        return 1

    w = 0
    ans = 0
    for _ in range(t):
        x = int(input())
        if x >= l:
            w = d

        if w > 0:
            ans += 1

        w -= 1

    print(max(0, ans - 1))


while not solve():
    ...
