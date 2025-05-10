import heapq

w = 60
h = 60


def id(x, y):
    return x + y * h


def dijkstra(g, start):
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

    return dist


def solve(t, n):
    b = [list(map(int, input().split())) for _ in range(n)]
    b = [[b1 + 30, b2 + 30] for b1, b2 in b]
    s = list(map(int, input().split()))
    s = [si + 30 for si in s]
    g = [[] for _ in range(w * h)]
    dire = [-1, 0, 1]

    for i in range(h):
        for j in range(w):
            for dy in dire:
                if i + dy == h:
                    continue
                for dx in dire:
                    if j + dx == w or dy + dx == 0:
                        continue
                    if [j + dx, i + dy] not in b:
                        g[id(j, i)].append((id(j + dx, i + dy), 1))

    print(len([i for i in dijkstra(g, id(s[0], s[1])) if i <= t]))


while True:
    t, n = map(int, input().split())
    if t == n == 0:
        exit()
    solve(t, n)
