import heapq


def dijkstra(g, n):
    distance = [float("inf")] * (n + 1)
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    distance[1] = 0
    heap = []

    heapq.heappush(heap, (distance[1], 1))
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

    return parent
