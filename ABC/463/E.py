# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def F(): return float(sys.stdin.readline().rstrip()) # 小数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def SI(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def DL(init, n, m): return [[init for _ in range(m)] for __ in range(n)]
def yes_no(b): return yes if b else no
def sigma(n): return (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on


def dijkstra(g, n, s):
    dist = [float("inf")] * (n)
    v = [False] * (n)
    dist[s] = 0
    heap = []

    heapq.heappush(heap, (dist[s], s))
    while heap:
        pos = heapq.heappop(heap)[1]

        if v[pos]:
            continue

        v[pos] = True
        for nex, cost in g[pos]:
            if dist[nex] > dist[pos] + cost:
                dist[nex] = dist[pos] + cost
                heapq.heappush(heap, (dist[nex], nex))

    return dist


N, M, Y = LI()
g = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, T = LI()
    u -= 1
    v -= 1

    g[u].append((v, T))
    g[v].append((u, T))

X = LI()

for i in range(N):
    g[i].append((N, X[i] + Y / 2))
    g[N].append((i, X[i] + Y / 2))

print(*[int(di) for di in dijkstra(g, N + 1, 0)[1:-1]])

"""
AC

ワープを頂点N+1への移動と言い換えて解く
iからN+1への重みをを X[i] + Y/2 で定義することで、ダイクストラで解ける
"""
