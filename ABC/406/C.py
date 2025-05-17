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
p = LI()

ud = []

for i in range(1, n):
    now = "U" if p[i - 1] < p[i] else "D"
    if len(ud) == 0:
        ud.append([now, 1])
        continue

    bef = ud[-1][0]
    if bef == now:
        ud[-1][1] += 1
    else:
        ud.append([now, 1])


ans = 0
udl = len(ud)
for i in range(1, udl - 1):
    if ud[i][0] == "U":
        continue

    bef = ud[i - 1][1]
    now = ud[i][1]
    aft = ud[i + 1][1]

    ans += bef * aft

print(ans)
