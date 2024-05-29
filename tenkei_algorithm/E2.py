# ダイクストラ法

import heapq


def init(n):
    distance = [float("inf")] * n
    visited = [False] * n
    return distance, visited


def dijkstra(g, start, n):
    distance, visited = init(n)

    distance[start] = 0
    heap = []
    heapq.heappush(heap, (distance[start], start))

    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in g[pos]:
            if distance[nex] > distance[pos] + cost:
                distance[nex] = distance[pos] + cost
                heapq.heappush(heap, (distance[nex], nex))

    return distance, visited


n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    v1, v2, c = map(int, input().split())
    g[v1].append((v2, c))

ans = 0
for i in range(n):
    distance, visited = dijkstra(g, i, n)
    for j in range(n):
        ans += distance[j]

print(ans)
