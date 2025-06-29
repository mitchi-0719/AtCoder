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
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, q = LI()
f = defaultdict(set)

for _ in range(q):
    t, a, b = LI()
    if t == 1:
        f[a].add(b)
    elif t == 2:
        if b in f[a]:
            f[a].remove(b)
    else:
        print(yes_no(b in f[a] and a in f[b]))
