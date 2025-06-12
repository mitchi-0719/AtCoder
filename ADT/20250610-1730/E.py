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
s_set = set()
s = []
t = []
idx = []

for i in range(n):
    si, ti = input().split()
    if si in s_set:
        continue

    s_set.add(si)
    s.append(si)
    t.append(-int(ti))
    idx.append(i)


print(list(zip(*sorted(zip(t, idx, s))))[1][0] + 1)
