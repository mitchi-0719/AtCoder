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


def dfs(g, cur, goal, path, visited):
    if cur == goal:
        print(*[p + 1 for p in path])
        return True

    visited[cur] = True
    for nex in g[cur]:
        path.append(nex)
        if not visited[nex] and dfs(g, nex, goal, path, visited):
            return True

        path.pop()

    return False


def solve():
    n, m, x, y = LI()
    g = [[] for _ in range(n)]

    for _ in range(m):
        u, v = [i - 1 for i in LI()]
        g[u].append(v)
        g[v].append(u)

    g = [sorted(gi) for gi in g]
    visited = [False for _ in range(n)]
    visited[x - 1] = True
    dfs(g, x - 1, y - 1, [x - 1], visited)


t = I()
for _ in range(t):
    solve()
