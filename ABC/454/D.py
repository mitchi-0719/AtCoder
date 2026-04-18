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
    a = S()
    b = S()

    n = len(a)
    m = len(b)

    ax = []
    bx = []

    tmp = ["(", "x", "x", ")"]
    for i in range(n - 3):
        if tmp == [a[i], a[i + 1], a[i + 2], a[i + 3]]:
            ax.append(i)

    a_skip = set()
    for axi in ax:
        j = 0
        while 1:
            st = axi - j
            ed = axi + 3 + j
            if st < 0 or ed >= n or not ((a[st], a[ed]) == ("(", ")")):
                break
            a_skip.add(st)
            a_skip.add(ed)
            j += 1

    a_fin = [a[i] for i in range(n) if i not in a_skip]

    for i in range(m - 3):
        if tmp == [b[i], b[i + 1], b[i + 2], b[i + 3]]:
            bx.append(i)

    b_skip = set()
    for bxi in bx:
        j = 0
        while 1:
            st = bxi - j
            ed = bxi + 3 + j
            if st < 0 or ed >= m or not ((b[st], b[ed]) == ("(", ")")):
                break
            b_skip.add(st)
            b_skip.add(ed)
            j += 1

    b_fin = [b[i] for i in range(m) if i not in b_skip]
    print(yes_no(a_fin == b_fin))


for _ in range(t):
    solve()
