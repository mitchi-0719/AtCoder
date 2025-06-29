# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
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
a = -1
b = 10
c = -1
d = 10

find_y = False
for i in range(10):
    s = S()
    if "#" in s:
        find_x = False
        for j, si in enumerate(s):
            if not find_x and si == "#":
                find_x = True
                c = j + 1
            if find_x and si == "." and d == 10:
                d = j
                break

        if not find_y:
            find_y = True
            a = i + 1
    else:
        if find_y and b == 10:
            b = i


print(a, b)
print(c, d)
