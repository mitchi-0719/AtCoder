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

s = S()
n = len(s)
ri = [i for i in range(n) if s[i] == "R"]
li = [i for i in range(n) if s[i] == "L"]

ans = [0 for _ in range(n)]
for i in range(n):
    if s[i] == "R":
        idx = bisect.bisect(li, i)
        l_idx = li[idx]
        ans[l_idx if abs(l_idx - i) % 2 == 0 else l_idx - 1] += 1
    else:
        idx = bisect.bisect(ri, i)
        r_idx = ri[idx - 1]
        ans[r_idx if abs(r_idx - i) % 2 == 0 else r_idx + 1] += 1


print(*ans)
