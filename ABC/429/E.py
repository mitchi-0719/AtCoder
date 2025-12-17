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

    p = []

    while not q.empty():
        pos = q.get()
        for nex in g[pos]:

            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.put(nex)
                if nex not in d:
                    p.append(dist[nex])
                    if len(p) == 2:
                        return sum(p)

    return dist


n, m = LI()
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = LI()
    g[u].append(v)
    g[v].append(u)

s = S()
d = set([i + 1 for i in range(n) if s[i] == "D"])
dists = dict()

for di in d:
    print(bfs(g, n, di))
