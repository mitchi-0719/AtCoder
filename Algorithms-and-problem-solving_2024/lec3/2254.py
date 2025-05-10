def solve2(n, t, get, time):
    set_g = set(get)
    if len(set_g) == 1 and list(set_g)[0]:
        return time

    m = float("inf")
    for i in range(n + 1):
        if get[i]:
            continue
        get[i] = True
        min_time = float("inf")
        for j in range(n):
            if get[j + 1]:
                min_time = min(min_time, t[j][i])
        min_time = min([k[i] for j, k in enumerate(t) if get[j + 1]])
        print(i, get, time, min_time)
        m = min(m, solve2(n, t, get, time + min_time))
    return m


def solve(n):
    t = []
    for _ in range(n):
        t.append(list(map(int, input().split())))
    print(t)
    ans = float("inf")
    for i in range(n):
        get = [False if i + 1 != j and j != 0 else True for j in range(n + 1)]
        ans = min(ans, solve2(n, t, get, t[i][0]))

    print(ans)


while True:
    n = int(input())
    if n == 0:
        exit()
    solve(n)
