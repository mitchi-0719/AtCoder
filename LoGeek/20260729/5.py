# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def F(): return float(sys.stdin.readline().rstrip()) # 小数値
def SI(): return sys.stdin.readline().rstrip() # 文字列
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def LF(): return list(map(float, sys.stdin.readline().rstrip().split())) # 小数値リスト
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def DL(init, n, m): return [[init for _ in range(m)] for __ in range(n)]
def yes_no(b): return yes if b else no
def sigma(n): return (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

N = I()
A = LI()

imos = [0] * (2 * 10**5 + 10)
for a in A:
    imos[0] += 1
    imos[a] -= 1

acc = list(accumulate(imos))
m = len(acc)

u = 0
ans = []
for i in range(m - 1):
    if acc[i] == 0:
        break

    ans.append(str(acc[i] % 10))
    acc[i + 1] += acc[i] // 10

print("".join(reversed(ans)))
