import heapq


def solve():
    n = int(input())
    if n == 0:
        return 1

    c = [list(map(int, input().split())) for _ in range(n)]
    for ci in c:
        heapq.heapify(ci)

    cur = 0
    cnt = 0

    while len(c) != 0:
        print(*c, cur, cnt)
        if len(c[cur]) == 0 or len(c[cur]) == 2 and c[cur][0] == c[cur][1]:
            c.pop(cur)
            if len(c) != 0:
                cur = cur % len(c)
            continue

        get = heapq.heappop(c[cur])
        nex = (cur + 1) % len(c)
        cnt += 1
        if get in c[nex]:
            c[nex].remove(get)
        else:
            heapq.heappush(c[nex], get)

        if len(c[cur]) == 0:
            c.pop(cur)
            cur = (cur - 1) % len(c)

        cur = (cur + 1) % len(c)

    print(cnt)


while not solve():
    ...
