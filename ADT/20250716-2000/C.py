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

r, c = LI()
b = [list(S()) for _ in range(r)]
dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(r):
    for j in range(c):
        if b[i][j] not in ("#", "."):
            n = int(b[i][j])
            b[i][j] = "."
            for di in dir:
                for x in range(n + 1):
                    for y in range(n - x + 1):
                        dx = x * di[0]
                        dy = y * di[1]
                        if (
                            0 <= i + dx < r
                            and 0 <= j + dy < c
                            and b[i + dx][j + dy] == "#"
                        ):
                            b[i + dx][j + dy] = "."

print("\n".join(["".join(bi) for bi in b]))
