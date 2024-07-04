# 解説AC

import heapq


def dijkstra(g, n, s):
    distance = [float("inf")] * (n + 1)
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    distance[s] = 0
    heap = []

    heapq.heappush(heap, (distance[s], s))
    while heap:
        pos = heapq.heappop(heap)[1]

        if visited[pos]:
            continue

        visited[pos] = True
        for nex, cost in g[pos]:
            if distance[nex] > distance[pos] + cost:
                distance[nex] = distance[pos] + cost
                parent[nex] = pos
                heapq.heappush(heap, (distance[nex], nex))

    return distance


n = int(input())
g = [[] for _ in range(n + 1)]

for i in range(1, n):
    a, b, x = map(int, input().split())
    g[i].append((i + 1, a))
    g[i].append((x, b))

print(dijkstra(g, n, 1)[-1])
