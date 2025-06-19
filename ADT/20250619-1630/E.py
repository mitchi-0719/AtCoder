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

h1, w1 = LI()
a = [LI() for _ in range(h1)]
h2, w2 = LI()
b = [LI() for _ in range(h2)]

for i in range(2**h1):
    for j in range(2**w1):
        tmp1 = []
        for k in range(h1):
            if i >> k & 1:
                tmp2 = []
                for l in range(w1):
                    if j >> l & 1:
                        tmp2.append(a[k][l])
                tmp1.append(tmp2)
        if b == tmp1:
            print("Yes")
            exit()

print("No")
