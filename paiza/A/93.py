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

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(y, x, k):
    if k == 0:
        return 0

    buf = c[y][x]
    mx_s = 0
    c[y][x] = 0
    for dx, dy in dir:
        if 0 <= x + dx < W and 0 <= y + dy < H and c[y + dy][x + dx] != 0:
            s = c[y + dy][x + dx]
            c[y + dy][x + dx] = 0
            mx_s = max(mx_s, s + dfs(y + dy, x + dx, k - 1) + buf)
            c[y + dy][x + dx] = s
    c[y][x] = buf
    return mx_s


H, W, K = LI()
c = [LI() for _ in range(H)]

mx = 0

for i in range(H):
    for j in range(W):
        mx = max(mx, dfs(i, j, K))

print(mx)
