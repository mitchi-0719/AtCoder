# AC

import queue

def BFS(g, start, n):
    dist = [-1] * (n+1)
    q = queue.Queue()
    dist[start] = 0
    q.put(start)

    while not q.empty():
        pos = q.get()
        for i in g[pos]:
            if dist[i] == -1:
                dist[i] = dist[pos]+1
                q.put(i)

    return max(dist)

n1, n2, m = map(int, input().split())

matrix = [list() for i in range(n1 + n2 + 1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

dist1 = BFS(matrix, 1, n1+n2)
dist2 = BFS(matrix, n1+n2, n1+n2)

print(dist1+dist2+1)
