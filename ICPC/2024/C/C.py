import queue
from collections import defaultdict


def bfs(g, n, start):

    # 初期化などなど
    dist = [-1] * (n + 1)
    q = queue.Queue()
    dist[start] = 0
    q.put(start)

    # 幅優先探索
    while not q.empty():
        pos = q.get()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.put(nex)

    return dist


w = 1000
w_all = w * 2 + 1


def id(i, j):
    return i * w_all + j


g = [[] for _ in range(id(w_all + 1, w_all + 1))]
move = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

for i in range(w_all + 1):
    for j in range(w_all + 1):
        for x, y in move:
            if 0 <= i + y <= w_all and 0 <= j + x <= w_all:
                g[id(i, j)].append(id(i + y, j + x))
                g[id(i + y, j + x)].append(id(i, j))

dist = bfs(g, id(w_all, w_all), id(w, w))

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(dist[id(x + w, y + w)])
