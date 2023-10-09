n, q = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

for i in range(q):
    x = int(input())

    b = 0
    t = len(a)-1
    m = (b + t)//2

    while 0 <= m < len(a) and b <= t:
        if x < a[m]:
            t = m-1
        elif x > a[m]:
            b = m+1
        else:
            break
        m = (b + t)//2

    if x == a[m]:
        print(len(a) - m)
    else:
        print(len(a) - m - 1)