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

# s = S()
s = "ABB" * (10**6) + "CB"
n = len(s)

i, j, k = 0, 0, 0
ans = 0

used = [False for _ in range(n)]
a_idx = [i for i in range(n) if s[i] == "A"]
b_idx = [i for i in range(n) if s[i] == "B"]
c_idx = [i for i in range(n) if s[i] == "C"]


for ai, i in enumerate(a_idx):

    bi = bisect.bisect(b_idx, i)
    try:
        j = b_idx[bi]
        while used[j]:
            bi += 1
            j = b_idx[bi]
    except:
        continue

    ci = bisect.bisect(c_idx, j)
    try:
        k = c_idx[ci]
        while used[k]:
            ci += 1
            k = c_idx[ci]
    except:
        continue

    try:
        if (s[i], s[j], s[k]) == ("A", "B", "C"):
            used[i] = True
            used[j] = True
            used[k] = True

            ans += 1
    except:
        continue

print(ans)
