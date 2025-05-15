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

s = list(S())
s_rev = list(reversed(s))
for i in range(len(s) - 1):
    if s_rev[i] + s_rev[i + 1] == "AW":
        s_rev[i] = "C"
        s_rev[i + 1] = "A"

print("".join(reversed(s_rev)))
