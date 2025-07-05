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

q = I()
a = []
i = 0

for _ in range(q):
    t, *query = LI()
    if t == 1:
        c, x = query
        a.append([c, x])
    else:
        k = query[0]
        s = 0
        while 1:
            if a[i][0] == k:
                s += a[i][0] * a[i][1]
                i += 1
                break
            elif a[i][0] > k:
                a[i][0] -= k
                s += a[i][1] * k
                break
            else:
                s += a[i][0] * a[i][1]
                k -= a[i][0]
                i += 1
        print(s)
