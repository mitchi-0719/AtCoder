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
inf = float("inf")
# fmt: on

s = S()
n = len(s)
st = 0
ed = 0
st_flag = False
ed_flag = False

for i in range(n):
    if s[i] == "a":
        if not st_flag:
            st += 1
    else:
        st_flag = True

    if s[~i] == "a":
        if not ed_flag:
            ed += 1
    else:
        ed_flag = True

s = "a" * max(0, ed - st) + s

for s1, s2 in zip(s, s[::-1]):
    if s1 != s2:
        print("No")
        exit()

print("Yes")
