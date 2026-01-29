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
s = list(S())
w = LI()

w, s = zip(*sorted(zip(w, s)))
w = list(w) + [inf]
cnt = s.count("1")
ans = cnt

for i in range(n):
    if s[i] == "1":
        cnt -= 1
    else:
        cnt += 1

    if w[i] != w[i + 1]:
        ans = max(ans, cnt)

    bef = w[i]

print(ans)

"""
ソートして並び替えたうえで、配列の各要素の間で分離できるかを考える。
区切りの前後で子供大人を判別するので、区切りを超えたときにその要素が子供なら+1, 大人なら-1をする

分離できる場合（区切りの前後の値が異なる）
    区切り以前の子供(0)の数 + 大人(1)の数がその時の解
分離できない場合（区切りの前後が同値）
    解を計算しない
"""
