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

n = S()
d = {0: 0, 1: 0, 2: 0}
m = sum([int(i) for i in n]) % 3

for si in n:
    i = int(si)
    d[i % 3] += 1


if m == 2:
    if d[2] >= 1 and list(d.values()) != [0, 0, 1]:
        print(1)
    elif d[1] >= 2 and list(d.values()) != [0, 2, 0]:
        print(2)
    else:
        print(-1)
elif m == 1:
    if d[1] >= 1 and list(d.values()) != [0, 1, 0]:
        print(1)
    elif d[2] >= 2 and list(d.values()) != [0, 0, 2]:
        print(2)
    else:
        print(-1)
else:
    print(0)
