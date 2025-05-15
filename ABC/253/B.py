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

h, w = LI()
s = [S() for _ in range(h)]
p = []

for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            p.append([i, j])

print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))
