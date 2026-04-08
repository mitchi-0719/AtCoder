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
yes = "Yes"
no = "No"

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

s = S()
t = S()

if s.replace("A", "") != t.replace("A", ""):
    print(-1)
    exit()

ans = 0
i, j = 0, 0
while 1:
    if len(s) <= i or len(t) <= j:
        ans += abs(len(s) - i) + abs(len(t) - j)
        break

    if s[i] == t[j]:
        i += 1
        j += 1
        continue

    if s[i] == "A":
        ans += 1
        i += 1
    elif t[j] == "A":
        ans += 1
        j += 1

print(ans)
