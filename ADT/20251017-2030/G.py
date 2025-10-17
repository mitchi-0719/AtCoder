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


def dfs(prev, i):
    if len(g[i]) == 1:
        return 1

    s = 0
    for gi in g[i]:
        if gi != prev:
            s += dfs(i, gi)
    return s + 1


n = I()
g = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = [i - 1 for i in LI()]
    g[u].append(v)
    g[v].append(u)

if len(g[0]) == 1:
    print(1)
    exit()

l = [dfs(0, i) for i in g[0]]
print(sum(l) - max(l) + 1)
