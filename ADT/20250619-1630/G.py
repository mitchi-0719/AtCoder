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

n = I()
s = list(S())
q = I()
is_upper = None
d = defaultdict(str)

for _ in range(q):
    t, x, c = LS()
    t = int(t)
    x = int(x) - 1
    if t == 1:
        d[x] = c
        s[x] = c
    elif t == 2:
        is_upper = False
        d.clear()
    else:
        is_upper = True
        d.clear()


for i in range(n):
    si = s[i]
    if "" != d[i]:
        print(d[i], end="")

    else:
        if is_upper == None:
            print(si, end="")
        elif is_upper:
            print(si.upper(), end="")
        else:
            print(si.lower(), end="")
