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
inf = float("inf")
# fmt: on

n, q = LI()
a = LI()
d = 0

for _ in range(q):
    t, x, y = [i - 1 for i in LI()]
    if t == 0:
        a[(x + d) % n], a[(y + d) % n] = a[(y + d) % n], a[(x + d) % n]
    elif t == 1:
        d -= 1
    else:
        print(a[(x + d) % n])
