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

q = I()
d = defaultdict(int)
s = set()
max_n = 0
min_n = float("inf")

for _ in range(q):
    query = LI()
    if query[0] == 1:
        x = query[1]
        d[x] += 1
        s.add(x)
        max_n = max(max_n, x)
        min_n = min(min_n, x)
    elif query[0] == 2:
        _, x, c = query
        d[x] = max(0, d[x] - c)
        if d[x] == 0 and x in s:
            s.remove(x)
            if len(s) == 0:
                max_n = 0
                min_n = float("inf")
            else:
                if max_n == x:
                    max_n = max(s)
                elif min_n == x:
                    min_n = min(s)
    else:
        print(max_n - min_n)
