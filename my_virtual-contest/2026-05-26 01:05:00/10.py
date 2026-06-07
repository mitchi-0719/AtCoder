# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

N = I()
a = LI()

d = defaultdict(int)

for ai in a:
    if ai % 4 == 0:
        d[4] += 1
    elif ai % 2 == 0:
        d[2] += 1
    else:
        d[-1] += 1

print(yes_no(d[-1] <= d[4] or (d[4] + 1 == d[-1] and N == (d[4] + d[-1]))))

"""
解説AC

奇数, 偶数, 4の倍数で個数をカウントして
パターン分けすれば良い
基本的には、4の倍数 >= 奇数
ただし、全体が奇数で4の倍数と奇数の差が1だったときも行ける（端を奇数として交互に全埋め）
"""
