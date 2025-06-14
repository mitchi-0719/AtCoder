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

n, q = LI()
x = LI()
b = [0] * n

for xi in x:
    if xi == 0:
        min_b = min(b)
        for i, bi in enumerate(b):
            if bi == min_b:
                b[i] += 1
                print(i + 1, end=" ")
                break
    else:
        b[xi - 1] += 1
        print(xi, end=" ")

print()
