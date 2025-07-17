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

h, w = LI()
s = [S() for _ in range(h)]

dir = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
st = "snuke"


def search(sx, sy):
    for dx, dy in dir:
        res = [[sy, sx]]
        for k in range(1, 5):
            y = sy + k * dy
            x = sx + k * dx
            if 0 <= y < h and 0 <= x < w and st[k] == s[y][x]:
                res.append([y, x])
            else:
                break
        else:
            return True, res
    return False, []


for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            flag, res = search(j, i)
            if flag:
                for r in res:
                    print(*[ri + 1 for ri in r])
                exit()
