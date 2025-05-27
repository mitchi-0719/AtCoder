def solve():
    n = int(input())
    if n == 0:
        return 1
    a = sorted(list(map(int, input().split())))

    bef = a[0]
    c = 1
    ans = 0
    for ai in a[1:]:
        if bef + 1 == ai:
            c += 1
        else:
            ans = max(ans, c)
            c = 1
        bef = ai

    print(max(ans, c))


while 1:
    if solve():
        break
