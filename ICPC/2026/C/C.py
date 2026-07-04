# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def F(): return float(sys.stdin.readline().rstrip()) # 小数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def SI(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def DL(init, n, m): return [[init for _ in range(m)] for __ in range(n)]
def yes_no(b): return yes if b else no
def sigma(n): return (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on


def solve():
    n = I()

    if n == 0:  # 終了条件
        return 1

    d = LI()

    ans = [inf] * n
    cur = d[0]
    ans[0] = 0

    for i in range(1, n):
        di = d[i]
        cur = min(cur, di)
        ans[i] = max(0, di - cur)

    d_rev = list(reversed(d))
    ans2 = [inf] * n
    cur = d_rev[0]
    ans2[0] = 0
    for i in range(1, n):
        di = d_rev[i]
        cur = min(cur, di)
        ans2[i] = min(ans2[i], max(0, di - cur))

    print(sum([min(a1, a2) for a1, a2 in zip(ans, reversed(ans2))]))


while not solve():
    ...
