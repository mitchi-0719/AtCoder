import heapq


def dijkstra(graph, n, m, s, g, frieze):
    dist = [float("inf")] * (n + 1)
    visited = [False] * (n + 1)
    dist[s] = 0
    heap = []

    heapq.heappush(heap, (dist[s], s))
    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in graph[pos]:
            if dist[nex] > dist[pos] + cost:
                dist[nex] = dist[pos] + cost
                heapq.heappush(heap, (dist[nex], nex))


def solve(n, m, l, k, a, h):
    frieze = []
    if l != 0:
        frieze = list(map(int, input().split()))

    g = [[] for _ in range(n)]
    for _ in range(k):
        x, y, t = map(int, input().split())
        if t > m:
            continue
        g[x].append((y, t))
        g[y].append((x, t))

    dijkstra(g, n, m, a, h, frieze)


while True:
    n, m, l, k, a, h = map(int, input().split())
    if n == m == l == k == a == h == 0:
        exit()
    solve(n, m, l, k, a, h)
