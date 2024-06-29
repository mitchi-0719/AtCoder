while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    s = [0 for _ in range(n)]
    for i in range(m):
        p = list(map(int, input().split()))
        for j in range(n):
            s[i] += p[i]
    print(s)
    print(max(s))
