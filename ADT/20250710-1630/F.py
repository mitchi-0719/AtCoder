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

n, t = LS()
n = int(n)
k = []
S = [S() for _ in range(n)]
for i, s in enumerate(S):
    if t == s:
        k.append(i + 1)
    elif len(t) - 1 == len(s):
        diff = 0
        for j in range(len(s)):
            if t[j + diff] != s[j]:
                if diff == 0:
                    if t[j + 1] != s[j]:
                        break
                    diff += 1
                else:
                    break
        else:
            k.append(i + 1)
    elif len(t) == len(s) - 1:
        diff = 0
        for j in range(len(t)):
            if t[j] != s[j + diff]:
                if diff == 0:
                    if t[j] != s[j + 1]:
                        break
                    diff += 1
                else:
                    break
        else:
            k.append(i + 1)
    elif len(s) == len(t):
        cnt = 0
        for j in range(len(s)):
            if t[j] != s[j]:
                if cnt == 0:
                    cnt += 1
                else:
                    break
        else:
            k.append(i + 1)

print(len(k))
print(*k)
