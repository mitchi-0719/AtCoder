# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


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


n = I()
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b, x = LI()
    x -= 1
    g[i].append((i + 1, a))
    g[i].append((x, b))


print(dijkstra(g, n, 0)[n - 1])
