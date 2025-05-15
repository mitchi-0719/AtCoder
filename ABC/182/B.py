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

n = int(input())
a = list(map(int, input().split()))
gcd = 0
ans = 0

for i in range(2, 1001):
    cnt = 0
    for ai in a:
        if ai % i == 0:
            cnt += 1
    if cnt > ans:
        gcd = i
        ans = cnt

print(gcd)
