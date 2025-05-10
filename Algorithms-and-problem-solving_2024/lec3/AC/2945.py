import heapq

w = 100
h = 100


def id(x, y):
    return x + y * h


def dijkstra(g, start, goal):
    dist = [float("inf")] * (w * h)
    visited = [False] * (w * h)
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (dist[start], start))

    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in g[pos]:
            if dist[nex] > dist[pos] + cost:
                dist[nex] = dist[pos] + cost
                heapq.heappush(heap, (dist[nex], nex))

    return dist[goal]


def solve(n, a, b, c, d, xy):

    g = [[] for _ in range(w * h)]

    for i in range(h):
        for j in range(1, w):
            g[id(j, i)].append(
                (id(j - 1, i), 0 if a <= j - 1 <= c and b <= i <= d else 1)
            )
            g[id(j - 1, i)].append((id(j, i), 0 if a <= j <= c and b <= i <= d else 1))

    for i in range(1, h):
        for j in range(w):
            g[id(j, i)].append(
                (id(j, i - 1), 0 if a <= j <= c and b <= i - 1 <= d else 1)
            )
            g[id(j, i - 1)].append((id(j, i), 0 if a <= j <= c and b <= i <= d else 1))

    ans = 0
    for i in range(n):
        x, y = xy[i]
        x2, y2 = xy[i + 1]
        ans += dijkstra(g, id(x, y), id(x2, y2))

    print(ans)


while True:
    n = int(input())
    if n == 0:
        exit()

    a, b, c, d = [int(i) - 1 for i in list(input().split())]
    xy = [list(map(int, input().split())) for _ in range(n + 1)]
    xy = [[x - 1, y - 1] for x, y in xy]
    solve(n, a, b, c, d, xy)
