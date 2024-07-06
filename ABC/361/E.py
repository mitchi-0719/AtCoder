import heapq


def dijkstra(g, n, s):
    distance = [float("inf")] * (n + 1)
    visited = [False] * (n + 1)
    route = [set() for _ in range(n + 1)]
    distance[s] = 0
    heap = []

    heapq.heappush(heap, (distance[s], s))
    route[s].add(s)
    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in g[pos]:
            if distance[nex] > distance[pos] + cost:
                distance[nex] = distance[pos] + cost
                route[nex] = route[pos].union(set([nex]))
                heapq.heappush(heap, (distance[nex], nex))

    return distance, route


n = int(input())
g = [[] for _ in range(n + 1)]
dists = [[] for _ in range(n + 1)]
routes = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())

    g[a].append((b, c))
    g[b].append((a, c))

for i in range(1, n + 1):
    dists[i], routes[i] = dijkstra(g, n, i)

print(dists, routes)
