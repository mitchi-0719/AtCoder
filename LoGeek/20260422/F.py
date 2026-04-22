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
yes = "Yes"
no = "No"

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

h, w = LI()
s = [list(S()) for _ in range(h)]
snuke = "snuke"

v = [[False for _ in range(w)] for _ in range(h)]


def dfs(prev, cur, i):
    x, y = cur
    if cur == (w - 1, h - 1) and s[y][x] == snuke[i % 5]:
        return True

    if s[y][x] != snuke[i % 5]:
        return False

    v[y][x] = True
    for dx, dy in dir4:
        nex = (x + dx, y + dy)
        if (
            0 <= x + dx < w
            and 0 <= y + dy < h
            and nex != prev
            and not v[y + dy][x + dx]
        ):
            res = dfs(cur, nex, i + 1)
            if res:
                return True

    v[y][x] = False
    return False


print(yes_no(dfs((-1, -1), (0, 0), 0)))
