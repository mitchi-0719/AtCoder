import heapq


def dijkstra(g, n, s, a):
    distance = [float("inf")] * n
    visited = [False] * n
    distance[s] = 0
    heap = []

    heapq.heappush(heap, (distance[s], s))
    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in g[pos]:
            if distance[nex] > distance[pos] + cost + a[pos]:
                distance[nex] = distance[pos] + cost + a[pos]
                heapq.heappush(heap, (distance[nex], nex))

    return distance


n, m = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]

for _ in range(m):
    u, v, b = map(int, input().split())
    g[u - 1].append((v - 1, b))
    g[v - 1].append((u - 1, b))

dist = dijkstra(g, n, 0, a)
for i, d in enumerate(dist[1:]):
    print(a[i + 1] + d, end=" ")

print()
