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

n = I()
a = LI()

d = defaultdict(int)
a_sort = sorted(a)

ans = set()

for ai in a:
    d[ai] += 1

mx = max(a)
mn = min(a)

if len(d) == 1:
    ans.add(mx)
    if d[mx] % 2 == 0:
        ans.add(mx * 2)


if n % 2 == 0:
    b = mx + mn
    for i in range(n):
        if b != a_sort[i] + a_sort[-(i + 1)]:
            break
    else:
        ans.add(b)


if len(d) != 1 and (n - d[mx]) % 2 == 0:
    mx_i = bisect.bisect_left(a_sort, mx)
    b = mx
    for i in range(mx_i):
        if mx != a_sort[i] + a_sort[-(i + 1 + d[mx])]:
            break
    else:
        ans.add(b)


print(*sorted(list(ans)))
