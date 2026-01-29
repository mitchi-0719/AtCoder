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
a = LI()
q = I()

acc = [0]

for i in range(1, n):
    if i % 2 == 0:
        acc.append(acc[-2] + a[i] - a[i - 1])
    else:
        acc.append(acc[-1])


for _ in range(q):
    l, r = LI()
    li = bisect.bisect_left(a, l)
    ri = bisect.bisect_left(a, r)
    ans = 0

    if ri - li == 0:
        if ri % 2 == 0:
            ans = r - l
    elif ri - li == 1:
        if ri % 2 == 0:
            ans = r - a[li]
        else:
            ans = a[li] - l
    else:
        if li % 2 == 1 and ri % 2 == 0:
            ans = acc[ri - 1] - acc[li] + r - a[ri - 1]
        elif li % 2 == ri % 2 == 1:
            ans = acc[ri] - acc[li]
        elif li % 2 == ri % 2 == 0:
            ans = acc[ri - 1] - acc[li] + a[li] - l + r - a[ri - 1]
        elif li % 2 == 0 and ri % 2 == 1:
            ans = acc[ri] - acc[li] + a[li] - l

    print(ans)


"""
可能性の考えられる全パターンを列挙することで求める。
大まかな数値は累積和を用いて表現し、細かい調整をそれぞれで行う

同じ区間内
    奇数ならば0
    偶数ならば、その差

隣接の区間内
    偶数側の差分のみ計算

基本的に、累積和で大まかな値を取得し、偶数側を調整する。
偶 ~ 奇
偶 ~ 偶
奇 ~ 偶
奇 ~ 奇
"""
