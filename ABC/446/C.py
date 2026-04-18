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

t = I()


def solve():
    n, d = LI()
    a = LI()
    b = LI()

    q = deque()

    for i in range(n):
        ai, bi = a[i], b[i]
        for _ in range(ai):
            q.append(i)
        for _ in range(bi):
            q.popleft()

        while len(q) != 0 and q[0] + d <= i:
            q.popleft()

    print(len(q))


for _ in range(t):
    solve()


"""
解説AC

stackで数えるだけのやつだね
"""
