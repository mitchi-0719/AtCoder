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

n = I()
s = S()
a = [0]
lr = [[-1, -1] for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if s[i] == "L":
        lr[i][0] = i + 1
        lr[i + 1][1] = i
    else:
        lr[i][1] = i + 1
        lr[i + 1][0] = i

print(lr)
