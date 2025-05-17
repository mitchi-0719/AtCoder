def solve():
    t, d, l = map(int, input().split())
    if t == d == l == 0:
        return True

    ans = 0
    lp = 0
    for _ in range(t):
        x = int(input())
        if x >= l:
            lp = d

        if lp > 0:
            ans += 1
        lp -= 1

    print(max(0, ans - 1))


while 1:
    if solve():
        break
