import queue


def bfs(g, n, start):

    # 初期化などなど
    dist = [-1] * (n + 1)
    q = queue.Queue()
    dist[start] = 0
    q.put(start)

    while not q.empty():
        pos = q.get()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.put(nex)

    return dist


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
goals = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    if b == 1:
        goals.append(a)

dist = bfs(g, n, 1)

ans = float("inf")
for gi in goals:
    if dist[gi] != -1:
        ans = min(ans, dist[gi] + 1)

print(ans if ans != float("inf") else -1)
