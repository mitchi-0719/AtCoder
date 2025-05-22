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

n, k = LI()
p = LI()
pn = [((pi * (pi + 1)) // 2) / pi for pi in p]

bef = pn[0]
s = sum(pn[:k])
mx = 0
j = 0

for i in range(n - k):
    mx = max(mx, s)

    s += pn[i + k] - bef
    bef = pn[i + 1]


mx = max(mx, s)
print(mx)
