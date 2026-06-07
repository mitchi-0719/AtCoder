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


def solve():
    w, h = LI()

    if w == h == 0:
        return 1

    q = deque()
    dist = [[0] * w for _ in range(h)]
    dist[0][0] = 1
    q.append((0, 0))

    wall = [LI() for _ in range(2 * h - 1)]
    while q:
        x, y = q.popleft()

        for dx, dy in dir4:
            if 0 <= x + dx < w and 0 <= y + dy < h and dist[y + dy][x + dx] == 0:
                if (
                    (dy == 1 and wall[y * 2 + 1][x] == 0)
                    or (dx == 1 and wall[y * 2][x] == 0)
                    or (dy == -1 and wall[y * 2 - 1][x] == 0)
                    or (dx == -1 and wall[y * 2][x - 1] == 0)
                ):
                    dist[y + dy][x + dx] = dist[y][x] + 1
                    q.append((x + dx, y + dy))

    print(dist[-1][-1])


while not solve():
    ...
