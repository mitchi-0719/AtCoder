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


def bfs(start, goal):
    q = deque([start])
    d = [[-1 for _ in range(w)] for __ in range(h)]
    i, j = start
    d[i][j] = 0

    goal_i = ()

    while q:
        i, j = q.popleft()
        for di, dj in dir4:
            ni = di + i
            nj = dj + j
            if 0 <= ni < h and 0 <= nj < w and s[ni][nj] != "X" and d[ni][nj] == -1:
                if s[ni][nj] == goal:
                    goal_i = (ni, nj)

                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))

    gi, gj = goal_i
    return goal_i, d[gi][gj]


h, w, n = LI()
cur = ()
s = []
for i in range(h):
    si = S()
    if "S" in si:
        cur = (i, si.index("S"))

    s.append(si)

ans = 0
for i in range(n):
    nex, d = bfs(cur, str(i + 1))

    cur = nex
    ans += d

print(ans)
