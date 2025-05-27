def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    a = list(map(int, input().split()))
    l = m // n
    ans = 0

    for ai in a:
        if ai < l:
            ans += ai
        else:
            ans += l

    print(ans)


while 1:
    if solve():
        break
