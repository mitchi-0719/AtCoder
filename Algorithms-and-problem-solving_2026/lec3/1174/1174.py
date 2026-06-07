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


colors = list(permutations((1, 2, 3, 4, 5, 6)))


def solve():
    h, w, c = LI()

    if h == w == c == 0:
        return 1

    def dfs(i, j, k, cur, color):
        if k >= 6:
            return 0

        cnt = 1
        if i + 1 < h:
            if p[i + 1][j] == cur:
                cnt += dfs(i + 1, j, k, cur, color)

            elif p[i + 1][j] == color[k]:
                cnt += dfs(i + 1, j, k + 1, color[k], color)

        if j + 1 < w:
            if p[i][j + 1] == cur:
                cnt += dfs(i, j + 1, k, cur, color)

            elif p[i][j + 1] == color[k]:
                cnt += dfs(i, j + 1, k + 1, color[k], color)

        return cnt

    p = [LI() for _ in range(h)]
    ans = 0
    for color in colors:
        t = dfs(0, 0, 0, p[0][0], color)
        if t > ans:
            print(color)
        ans = max(ans, dfs(0, 0, 0, p[0][0], color))

    print(ans)


while not solve():
    ...
