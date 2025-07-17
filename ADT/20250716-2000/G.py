# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
inf = float("inf")
# fmt: on


def bfs(g, n, start):
    dist = [-1] * (n + 1)
    q = queue.Queue()
    dist[start] = 0
    q.put(start)

    while not q.empty():
        pos = q.get()
        for nex in g[pos]:
            if nex == start:
                return dist[pos] + 1
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.put(nex)

    return -1


n, m = LI()
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = [i - 1 for i in LI()]
    g[a].append(b)

print(bfs(g, n, 0))
