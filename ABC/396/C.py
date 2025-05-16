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

n, m = LI()
b = sorted(LI(), reverse=True)
w = sorted(LI(), reverse=True)

bs = n - bisect.bisect(list(reversed(b)), 0) - 1
b_acc = list(accumulate(b))
w_acc = list(accumulate(w))

b_max = b_acc[-1] if bs == m else b_acc[bs]
ans = max(0, b_max)

for i in range(min(n, m)):
    if i <= bs:
        ans = max(ans, w_acc[i] + b_max)
    else:
        ans = max(ans, w_acc[i] + b_acc[i])

print(ans)
