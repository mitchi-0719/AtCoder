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

n = I()
b = bin(n)[2:][::-1]
bl = [i for i in range(len(b)) if b[i] == "1"]
l = len(bl)
ans = []

for i in range(2**l):
    li = []
    for j in range(l):
        if (i >> j) & 1:
            li.append(j)

    num = 0
    for j in range(len(li)):
        num += 2 ** bl[li[j]]

    ans.append(num)

ans = sorted(ans)
for a in ans:
    print(a)
