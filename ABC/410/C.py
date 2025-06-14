# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, q = LI()
a = [i + 1 for i in range(n)]

d = 0
for _ in range(q):
    t, *query = LI()
    if t == 1:
        p, x = query
        a[(d + p - 1) % n] = x
    elif t == 2:
        print(a[(d + query[0] - 1) % n])
    else:
        d += query[0]
