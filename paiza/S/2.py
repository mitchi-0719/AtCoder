# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
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


def id(i, j):
    return j + i * N


N, M = LI()
s = [list(S().split()) for _ in range(M)]
G = [set() for _ in range(N * M)]

st = -1
gl = -1

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(M):
    for j in range(N):
        if s[i][j] == "1":
            continue

        if s[i][j] == "s":
            st = id(i, j)
        elif s[i][j] == "g":
            gl = id(i, j)

        for di, dj in dir:
            if 0 <= i + di < M and 0 <= j + dj < N and s[i + di][j + dj] != "1":
                G[id(i, j)].add(id(i + di, j + dj))
                G[id(i + di, j + dj)].add(id(i, j))

dist = bfs(G, N * M, st)
print(dist[gl] if dist[gl] != -1 else "Fail")
