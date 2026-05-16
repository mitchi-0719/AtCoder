# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

n = I()
g = [[] for _ in range(n)]

for i in range(n):
    [u, k, *v] = LI()
    for vi in sorted(v):
        g[u - 1].append(vi - 1)

q = deque([0])
d = [-1 for _ in range(n)]
d[0] = 0

while q:
    v = q.popleft()
    for nex in g[v]:
        if d[nex] == -1:
            d[nex] = d[v] + 1
            q.append(nex)

for i in range(n):
    print(i + 1, d[i])
