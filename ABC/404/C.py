# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def dfs(g, i, visited):
    if visited[i]:
        return

    visited[i] = True
    for v in g[i]:
        dfs(g, v, visited)


n, m = LI()
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = LI()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

visited = [False for _ in range(n)]
dfs(g, 0, visited)
if [len(gi) for gi in g] != [2] * n or visited != [True] * n:
    print("No")
    exit()

print("Yes")
