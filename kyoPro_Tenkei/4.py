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

h, w = LI()
a = [LI() for _ in range(h)]
r_sum = [sum([a[i][j] for j in range(w)]) for i in range(h)]
c_sum = [sum([a[i][j] for i in range(h)]) for j in range(w)]

for i in range(h):
    tmp = []
    for j in range(w):
        tmp.append(r_sum[i] + c_sum[j] - a[i][j])
    print(*tmp)
