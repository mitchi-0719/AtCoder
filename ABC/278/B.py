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

h, m = LI()

while 1:
    ms = str(m).zfill(2)
    hs = str(h).zfill(2)

    if int(hs[0] + ms[0]) < 24 and int(hs[1] + ms[1]) < 60:
        print(hs, ms)
        break

    m = (m + 1) % 60
    if m == 0:
        h = (h + 1) % 24
