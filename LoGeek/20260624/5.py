# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def F(): return float(sys.stdin.readline().rstrip()) # 小数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def SI(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def DL(init, n, m): return [[init for _ in range(m)] for __ in range(n)]
def yes_no(b): return yes if b else no
def sigma(n): return (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

N = I()
a = LI()

m = defaultdict(int)

for ai in a:
    m[ai % 4] += 1


if N % 2 == 0:
    odd = m[1] + m[3]
    print(yes_no(m[0] >= odd))
else:
    odd = m[1] + m[3]
    print(yes_no(m[0] + 1 >= odd and m[0] + odd == N or m[0] >= odd))


# if N == 1:
#     print(yes_no(a[0] % 4 == 0))
# elif N <= 3:
#     print(yes_no(any([ai % 4 == 0 for ai in a]) or all([ai % 2 == 0 for ai in a])))
# elif N == 5:
#     print(
#         yes_no(
#             len([ai for ai in a if ai % 4 == 0]) >= 2
#             or all([ai % 2 == 0 for ai in a] or (m[0] >= 1 and m[2] >= 3))
#         )
#     )
# else:
#     odd = m[1] + m[3]
#     print(yes_no(m[0] >= odd))
