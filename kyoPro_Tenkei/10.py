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

n = I()
cp = [LI() for _ in range(n)]

c1 = [0] + list(accumulate([cp[i][1] if cp[i][0] == 1 else 0 for i in range(n)]))
c2 = [0] + list(accumulate([cp[i][1] if cp[i][0] == 2 else 0 for i in range(n)]))

q = I()
for _ in range(q):
    l, r = LI()
    print(c1[r] - c1[l - 1], c2[r] - c2[l - 1])
