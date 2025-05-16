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

sys.setrecursionlimit(10**8)
mod = 998244353
inf = 2**70
# fmt: on


def dfs(g, i, n, visited, x):
    if i == n:
        return x

    ans = inf
    for nex, w in g[i]:
        if visited[i]:
            continue
        visited[i] = True
        new_x = x ^ w
        ans = min(dfs(g, nex, n, visited, new_x), ans)
        visited[i] = False

    return ans


n, m = LI()
g = [[] for _ in range(n)]


for _ in range(m):
    u, v, w = LI()
    u -= 1
    v -= 1

    g[u].append((v, w))
    g[v].append((u, w))

visited = [False for _ in range(n)]
print(dfs(g, 0, n - 1, visited, 0))
