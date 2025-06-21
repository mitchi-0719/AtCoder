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
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, q = LI()
a = LI()
b = [1] * n
ans = 0

for ai in a:
    ai -= 1
    b[ai] *= -1
    if b[ai] == -1:
        if ai == 0:
            if n == 1 or b[ai + 1] == 1:
                ans += 1
        elif ai == n - 1:
            if n == 1 or b[ai - 1] == 1:
                ans += 1
        elif b[ai - 1] == 1 and b[ai + 1] == 1:
            ans += 1
        elif b[ai - 1] == -1 and b[ai + 1] == -1:
            ans -= 1
    else:
        if ai == 0:
            if n == 1 or b[ai + 1] == 1:
                ans -= 1
        elif ai == n - 1:
            if n == 1 or b[ai - 1] == 1:
                ans -= 1
        elif b[ai - 1] == 1 and b[ai + 1] == 1:
            ans -= 1
        elif b[ai - 1] == -1 and b[ai + 1] == -1:
            ans += 1

    print(ans)
