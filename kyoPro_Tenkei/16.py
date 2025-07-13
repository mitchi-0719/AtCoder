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
a, b, c = LI()
ans = inf

for i in range(10000):
    if n < a * i:
        break
    for j in range(10000):
        if n < a * i + b * j:
            break
        if (n - (a * i + b * j)) % c == 0:
            k = (n - (a * i + b * j)) // c
            ans = min(ans, i + j + k)

print(ans)
