def solve(n, p):
    infect = set([p])
    for _ in range(n):
        a, b = map(int, input().split())
        if a in infect:
            infect.add(b)
        elif b in infect:
            infect.add(a)

    print(len(infect))


while True:
    m, n, p = map(int, input().split())
    if m == n == p == 0:
        exit()

    solve(n, p)
