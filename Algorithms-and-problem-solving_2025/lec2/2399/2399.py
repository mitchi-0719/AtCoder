def solve():
    n = int(input())
    if n == 0:
        return True

    m, p = [], []
    for _ in range(n):
        [mi, *pi] = list(map(int, input().split()))
        m.append(mi)
        p.append(set(pi))

    [_, *l] = list(map(int, input().split()))
    l = set(l)

    ans = None
    for i in range(n):
        if l.issubset(p[i]):
            if ans == None:
                ans = i + 1
            else:
                print(-1)
                return

    print(ans if ans != None else -1)


while 1:
    if solve():
        break
