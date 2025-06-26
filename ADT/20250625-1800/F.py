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

n = I()
a = LI()
m = I()
b = LI()
l = I()
c = LI()
q = I()
x = LI()

s = set()
for ai in a:
    for bi in b:
        for ci in c:
            s.add(ai + bi + ci)

for xi in x:
    print(yes_no(xi in s))
