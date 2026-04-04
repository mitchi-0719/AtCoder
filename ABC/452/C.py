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

n = I()
ab = []
d = defaultdict(list)
for _ in range(n):
    a, b = LI()
    ab.append([a, b])
    d[a].append(b)

l = [[set() for _ in range(11)] for _ in range(11)]

m = I()
s = []
for _ in range(m):
    si = S()
    s.append(si)
    ln = len(si)
    for b in d[ln]:
        l[ln][b - 1].add(si[b - 1])


def solve(s):
    ln = len(s)
    if ln != n:
        print(no)
        return

    for i, c in enumerate(s):
        a, b = ab[i]
        if c not in l[a][b - 1]:
            print(no)
            return

    print(yes)


for si in s:
    solve(si)
