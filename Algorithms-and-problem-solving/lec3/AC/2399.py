def solve(n, g, l):
    ans = -1
    for i, gl in enumerate(g):
        if set(l).issubset(gl):
            if ans == -1:
                ans = i
            else:
                print(-1)
                return
    print(ans)


while True:
    n = int(input())
    if n == 0:
        exit()

    k = []
    g = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        li = list(map(int, input().split()))
        for p in li[1:]:
            g[i].append(p)

    li = list(map(int, input().split()))
    l = [i for i in li[1:]]
    solve(n, g, l)
