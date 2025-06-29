# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


n, m, x, y = LI()
xy = [LI() for _ in range(n)]
dx = defaultdict(SortedSet)
dy = defaultdict(SortedSet)
nx, ny = x, y


def is_in_range(start, end, x):
    if start < end:
        return start <= x <= end
    return end <= x <= start


for x, y in xy:
    dx[x].add(y)
    dy[y].add(x)

ans = 0
for _ in range(m):
    d, c = LS()
    c = int(c)

    if d == "U":
        s = ny
        e = ny + c

        for i in range(len(dx[nx])):
            if is_in_range(s, e, dx[nx][i]):
                dyi = dx[nx][i]
                dx[nx].remove(dyi)
                dy[dyi].remove(nx)
                ans += 1
        ny += c

    elif d == "D":
        s = ny
        e = ny - c

        for i in range(len(dx[nx])):
            if is_in_range(s, e, dx[nx][i]):
                dyi = dx[nx][i]
                dx[nx].remove(dyi)
                dy[dyi].remove(nx)
                ans += 1

        ny -= c

    elif d == "L":
        s = nx
        e = nx - c

        for i in range(len(dy[ny])):
            if is_in_range(s, e, dy[ny][i]):
                dxi = dy[ny][i]
                dy[ny].remove(dxi)
                dx[dxi].remove(ny)
                ans += 1

        nx -= c

    elif d == "R":
        s = nx
        e = nx + c

        for i in range(len(dy[ny])):
            if is_in_range(s, e, dy[ny][i]):
                dxi = dy[ny][i]
                dy[ny].remove(dxi)
                dx[dxi].remove(ny)
                ans += 1

        nx += c


print(nx, ny, ans)
