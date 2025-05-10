# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

r, x = LI()

if x == 1:
    print(yes_no(1600 <= r <= 2999))
else:
    print(yes_no(1200 <= r <= 2399))
