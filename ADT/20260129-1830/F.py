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

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

n, a, b = LI()
s = S()
st = 0 if s[0] == "a" else 1

cnt = []

bef = ""
for si in s:
    if si == bef:
        cnt[-1] += 1
    else:
        cnt.append(1)

    bef = si

l, r = 0, 0
ans = 0

ab_total = {"a": 0, "b": 0}
i = 0
print(ab_total)
while 1:
    if ab_total["a"] >= a and ab_total["b"] < b:
        ans += 1

    if ab_total["a"] < a:
        r += 1
        if r == n:
            break
        ab_total[s[r]] += 1
    else:
        ab_total[s[l]] -= 1
        l += 1

    print(ab_total, ans)

print(ans)
