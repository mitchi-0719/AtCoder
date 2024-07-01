import queue
from collections import defaultdict

memo = defaultdict(lambda: [])


def bfs(start):

    if len(memo[start]) != 0:
        return memo[start]

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

    memo[start] = dist
    return memo[start]


n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(q):
    d, c = map(int, input().split())
    dist = []
    if len(memo[d]) != 0:
        print("Road" if memo[d][c] % 2 == 1 else "Town")
    elif len(memo[c]) != 0:
        print("Road" if memo[c][d] % 2 == 1 else "Town")
    else:
        print("Road" if bfs(d)[c] % 2 == 1 else "Town")
