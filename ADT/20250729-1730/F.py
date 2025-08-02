# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
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
lr = [LI() for _ in range(n)]
d = [r - l for l, r in lr]
l = [lr[i][0] for i in range(n)]
l_sum = sum(l)

if l_sum == 0:
    print("Yes")
    print(*l)
    exit()

if l_sum > 0:
    print("No")
    exit()

x = [*l]
for i in range(n):
    if l_sum + d[i] < 0:
        x[i] += d[i]
        l_sum += d[i]
    else:
        x[i] -= l_sum
        print("Yes")
        print(*x)
        exit()

print("No")
