"""
g: 隣接リスト
n: 頂点数
s: スタート

distance: sから各頂点への距離
visited: 訪れたかどうか
parent: 頂点iの親
"""

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
