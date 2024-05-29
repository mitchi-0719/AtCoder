import heapq

MAX = 10 * 10


def dijkstra(graph, start):
    # 始点から各頂点への最短距離を格納する辞書
    shortest_distances = {vertex: float("infinity") for vertex in graph}
    shortest_distances[start] = 0
    # 未確定の頂点を管理する優先度付きキュー
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 現在の頂点から隣接する頂点への距離を確認し、必要に応じて更新
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


def solve(n, a, b, c, d, xy):
    w = 10
    h = 10

    g = [[] for _ in range(w * h)]

    def id(x, y):
        return x + y * h

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

    dijkstra()


while True:
    n = int(input())
    if n == 0:
        exit()

    a, b, c, d = [int(i) - 1 for i in list(input().split())]
    xy = [list(map(int, input().split())) for _ in range(n + 1)]
    xy = [[x - 1, y - 1] for x, y in xy]
    solve(n, a, b, c, d, xy)
